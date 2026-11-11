# Instalador de agentes e skills nativos do Claude Code; nao usa /plugin.
# Executar de uma copia revisada deste repositorio em um projeto autorizado.
[CmdletBinding()]
param(
  [Parameter(Mandatory=$true)]
  [string]$ProjectPath,
  [switch]$Force
)
$ErrorActionPreference = 'Stop'
$SourceRoot = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$ProjectRoot = (Resolve-Path -LiteralPath $ProjectPath).Path
if ($ProjectRoot.TrimEnd('\','/') -eq $SourceRoot.TrimEnd('\','/')) {
  throw 'O destino deve ser o projeto Claude Code que contem seu MCP, e nao a pasta do toolkit.'
}
$PluginRoot = Join-Path $SourceRoot 'plugins/market-intelligence'
$AgentSource = Join-Path $PluginRoot 'agents'
$SkillSource = Join-Path $PluginRoot 'skills'
if (-not ((Test-Path $AgentSource -PathType Container) -and (Test-Path $SkillSource -PathType Container))) {
  throw 'Pacote incompleto: agents/ ou skills/ nao encontrados.'
}
$ClaudeRoot = Join-Path $ProjectRoot '.claude'
$Planned = @()
foreach ($agent in (Get-ChildItem -LiteralPath $AgentSource -Filter '*.md' -File)) {
  $Planned += [pscustomobject]@{ Source=$agent.FullName; Relative=('agents/' + $agent.Name) }
}
foreach ($skill in (Get-ChildItem -LiteralPath $SkillSource -Directory)) {
  foreach ($file in (Get-ChildItem -LiteralPath $skill.FullName -Recurse -File)) {
    $relInSkill = $file.FullName.Substring($skill.FullName.Length).TrimStart('\','/')
    $Planned += [pscustomobject]@{ Source=$file.FullName; Relative=('skills/' + $skill.Name + '/' + ($relInSkill -replace '\','/')) }
  }
}
if ($Planned.Count -eq 0) { throw 'Nenhum agente ou skill encontrado.' }
# Confere todos os conflitos antes da primeira copia.
$Conflicts = @()
foreach ($file in $Planned) {
  $dest = Join-Path $ClaudeRoot $file.Relative
  if (Test-Path -LiteralPath $dest -PathType Leaf) {
    $a = (Get-FileHash -LiteralPath $file.Source -Algorithm SHA256).Hash
    $b = (Get-FileHash -LiteralPath $dest -Algorithm SHA256).Hash
    if ($a -ne $b) { $Conflicts += $file.Relative }
  }
}
if ($Conflicts.Count -gt 0 -and -not $Force) {
  throw ("Arquivos existentes diferem: " + ($Conflicts -join ', ') + ". Nada foi copiado. Revise ou execute com -Force (backups).")
}
$stamp = Get-Date -Format 'yyyyMMdd-HHmmss'
$copied = 0; $skipped = 0
foreach ($file in $Planned) {
  $dest = Join-Path $ClaudeRoot $file.Relative
  New-Item -Path (Split-Path -Path $dest -Parent) -ItemType Directory -Force | Out-Null
  if (Test-Path -LiteralPath $dest -PathType Leaf) {
    $a = (Get-FileHash -LiteralPath $file.Source -Algorithm SHA256).Hash
    $b = (Get-FileHash -LiteralPath $dest -Algorithm SHA256).Hash
    if ($a -eq $b) { $skipped++; continue }
    Copy-Item -LiteralPath $dest -Destination ($dest + '.backup-' + $stamp) -ErrorAction Stop
  }
  Copy-Item -LiteralPath $file.Source -Destination $dest -Force
  $copied++
}
$gitignore = Join-Path $ProjectRoot '.gitignore'
$ignore = '/reports/powerbi-model-audit/'
$existing = if (Test-Path -LiteralPath $gitignore) { Get-Content -LiteralPath $gitignore } else { @() }
if (-not ($existing | Where-Object { $_.Trim() -eq $ignore })) {
  Add-Content -LiteralPath $gitignore -Value "`n# Auditoria interna do Power BI - nao versionar`n$ignore" -Encoding UTF8
}
Write-Host ('Concluido: ' + $copied + ' arquivos novos/atualizados; ' + $skipped + ' inalterados.') -ForegroundColor Green
Write-Host ('Projeto: ' + $ProjectRoot)
Write-Host 'MCP, settings, credenciais e PBIX existentes preservados.'
Write-Host 'Reinicie a sessao local se necessario. No Claude Code execute: /mapear-modelo'
Write-Warning 'Em sessoes cloud/Cowork as skills locais podem nao ser carregadas. Use Claude Code local.'
