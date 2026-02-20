# safe-share

Encrypted sharing tool for creators who want feedback without fear of copying.

## Features

- **Encrypt files/text** with strong encryption and generate sharing keys
- **Invisible watermarks** to track content source and prevent unauthorized copying
- **Decrypt and verify** watermark integrity to identify leaks

## Installation


## Usage

### Encrypt content with watermark


### Decrypt content


### Add watermark only


## How it works

1. **Encryption**: Uses Fernet symmetric encryption (AES-128) to protect content
2. **Watermark**: Embeds invisible zero-width characters with hashed user ID
3. **Tracking**: If content leaks, watermark reveals the source

## Security Notes

- Keep encryption keys private
- Share keys only through secure channels
- Watermarks are detectable by technical users but invisible in normal viewing
- This tool helps deter casual copying, not prevent determined attackers

## Use Cases

- Share business plans with potential investors
- Get feedback on code without fear of theft
- Distribute beta content to trusted testers
- Protect creative work during collaboration
# 安装
pip install -r requirements.txt

# 加密并添加水印（给不同人分享时用不同 watermark-id）
python main.py encrypt proposal.txt --watermark-id "investor_alice" --output encrypted.bin

# 解密时会自动检测水印
python main.py decrypt encrypted.bin "密钥" --output result.txt