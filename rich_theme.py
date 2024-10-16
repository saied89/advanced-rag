from rich.theme import Theme

custom_theme = Theme({
    "repr.own": "bright_yellow",            # Class names
    "repr.tag_name": "bright_yellow",       # Adjust tag names which might still be purple
    "repr.call": "bright_yellow",           # Function calls and other symbols
    "repr.str": "bright_green",             # String representation
    "repr.number": "bright_red",            # Numbers
    "repr.none": "bright_blue",             # None
    "repr.attrib_name": "bright_yellow",    # Attribute names
    "repr.attrib_value": "bright_blue"      # Attribute values
})

