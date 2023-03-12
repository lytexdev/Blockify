destruction_rate = {}


def add_block(block):
    """Add block to destruction rate"""
    if block not in destruction_rate:
        destruction_rate[block] = 1


def edit_block(block, rate: int):
    """Edit block destruction rate"""
    if block in destruction_rate:
        destruction_rate[block] = rate


def remove_block(block):
    """Remove block from destruction rate"""
    if block in destruction_rate:
        del destruction_rate[block]
