
🖼️ Array of ASCII art diagrams

    ( o.o )
     > ^ <
    """,

    r"""
     _______
    |       |
    |       O
    |      /|\
    |      / \
    |
    =========
    """,

    r"""
    _______
   /       \
  |  (• ◡•)  |
   \_______/
    """,

    r"""
     __
    /  \
   |    |
   |____|
  /      \
 /________\ascii_art_diagrams = [
    r"""
     /\_/\
    """
]

# 📝 Array of creative writing prompts
story_prompts = [
    "Write a story about a robot who wants to be human.",
    "Describe a world where plants can talk to people.",
    "Create a mystery involving a time-traveling detective.",
    "Tell a bedtime story set on a spaceship.",
    "Imagine a dragon who’s afraid of fire.",
    "Write about a kid who finds a magical notebook.",
    "Narrate a short poem about loneliness and the moon.",
    "Describe an ancient civilization powered by sound."
]

while True:
    user_input= input("\n Type 'draw', 'draw' 'exit").strip().lower()
    if UserWarning="exit":
        print('goodbye')
        breake
    elif user_input.startswith("draw")
        select_art = random.choice(asscii_art_diagram)
        print("\n Here is a random ACCii drawing")
        print(select_art)

    elif user_input.startwith("write"):
        selected_prompt= random.choice(story_prompt)
        print("\n Here is randaom ACII writing")
        print(selected_prompt)
    else:
        print("\ninvalid command try 'draw' 'write, 'exit'")       