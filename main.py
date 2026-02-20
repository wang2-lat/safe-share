import typer
from rich.console import Console
from pathlib import Path
from crypto_utils import encrypt_content, decrypt_content
from watermark_utils import add_watermark, verify_watermark

app = typer.Typer(help="Encrypted sharing tool with watermark tracking")
console = Console()

@app.command()
def encrypt(
    input_path: Path = typer.Argument(..., help="File or text to encrypt"),
    output: Path = typer.Option("encrypted.bin", help="Output file path"),
    watermark_id: str = typer.Option(None, help="Watermark ID to embed")
):
    """Encrypt file/text and generate sharing key"""
    try:
        if input_path.exists():
            content = input_path.read_text()
        else:
            content = str(input_path)
        
        if watermark_id:
            content = add_watermark(content, watermark_id)
            console.print(f"[green]Watermark '{watermark_id}' embedded[/green]")
        
        encrypted_data, key = encrypt_content(content)
        output.write_bytes(encrypted_data)
        
        console.print(f"[green]Encrypted successfully![/green]")
        console.print(f"Output: {output}")
        console.print(f"[yellow]Share Key: {key}[/yellow]")
        console.print("[red]Keep this key safe! Share it only with trusted recipients.[/red]")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)

@app.command()
def decrypt(
    input_path: Path = typer.Argument(..., help="Encrypted file"),
    key: str = typer.Argument(..., help="Decryption key"),
    output: Path = typer.Option("decrypted.txt", help="Output file path")
):
    """Decrypt file and verify watermark"""
    try:
        encrypted_data = input_path.read_bytes()
        content = decrypt_content(encrypted_data, key)
        
        watermark_id = verify_watermark(content)
        if watermark_id:
            console.print(f"[yellow]Watermark detected: {watermark_id}[/yellow]")
            console.print("[red]This content is tracked. Unauthorized sharing can be traced.[/red]")
        
        output.write_text(content)
        console.print(f"[green]Decrypted successfully![/green]")
        console.print(f"Output: {output}")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)

@app.command()
def watermark(
    input_path: Path = typer.Argument(..., help="File to watermark"),
    watermark_id: str = typer.Argument(..., help="Watermark ID"),
    output: Path = typer.Option("watermarked.txt", help="Output file path")
):
    """Add invisible watermark to file"""
    try:
        content = input_path.read_text()
        watermarked = add_watermark(content, watermark_id)
        output.write_text(watermarked)
        
        console.print(f"[green]Watermark '{watermark_id}' added successfully![/green]")
        console.print(f"Output: {output}")
    except Exception as e:
        console.print(f"[red]Error: {e}[/red]")
        raise typer.Exit(1)

if __name__ == "__main__":
    app()
