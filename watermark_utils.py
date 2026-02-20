import hashlib

WATERMARK_PREFIX = "\u200b\u200c\u200d"  # Zero-width characters
WATERMARK_SUFFIX = "\u200d\u200c\u200b"

def add_watermark(content: str, watermark_id: str) -> str:
    """Add invisible watermark to content"""
    watermark_hash = hashlib.sha256(watermark_id.encode()).hexdigest()[:16]
    watermark = f"{WATERMARK_PREFIX}{watermark_hash}{WATERMARK_SUFFIX}"
    return watermark + content

def verify_watermark(content: str) -> str | None:
    """Extract and verify watermark from content"""
    if not content.startswith(WATERMARK_PREFIX):
        return None
    
    try:
        end_idx = content.index(WATERMARK_SUFFIX)
        watermark_hash = content[len(WATERMARK_PREFIX):end_idx]
        return watermark_hash
    except ValueError:
        return None
