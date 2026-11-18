# Export the November deck's figure slides to img/ as 1920 px wide PNGs.
# Needs Windows with PowerPoint installed.
# Usage: powershell -ExecutionPolicy Bypass -File scripts\export-figures.ps1 -Deck "C:\path\to\deck.pptx"
param([Parameter(Mandatory)][string]$Deck)

# Deck slide number -> file name in img/
$slides = @{ 5 = 'skills'; 8 = 'marvel'; 9 = 'vault'; 10 = 'hub'; 11 = 'orchestrator'; 12 = 'herdr' }

$out = [IO.Path]::GetFullPath((Join-Path $PSScriptRoot '..\img'))
New-Item -ItemType Directory -Force $out | Out-Null

$ppt = New-Object -ComObject PowerPoint.Application
try {
    # ReadOnly, Untitled = false, WithWindow = false
    $pres = $ppt.Presentations.Open((Resolve-Path $Deck).Path, $true, $false, $false)
    $height = [int](1920 * $pres.PageSetup.SlideHeight / $pres.PageSetup.SlideWidth)
    foreach ($s in $slides.GetEnumerator()) {
        $file = Join-Path $out "$($s.Value).png"
        $pres.Slides.Item($s.Key).Export($file, 'PNG', 1920, $height)
        Write-Host "slide $($s.Key) -> img\$($s.Value).png"
    }
    $pres.Close()
} finally {
    # Leave PowerPoint running if the user had other decks open.
    if ($ppt.Presentations.Count -eq 0) { $ppt.Quit() }
}
