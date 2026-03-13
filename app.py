import random
import time
from datetime import datetime

import streamlit as st

st.set_page_config(
    page_title="Rosa's Dream Closet",
    page_icon="💖",
    layout="wide",
)

# -----------------------------
# Data
# -----------------------------
BAGS = [
    {"name": "Chanel Classic Flap", "brand": "Chanel", "vibe": "Elegant princess energy", "emoji": "🖤"},
    {"name": "Dior Saddle Bag", "brand": "Dior", "vibe": "Fashion-girl icon", "emoji": "✨"},
    {"name": "Louis Vuitton Speedy", "brand": "Louis Vuitton", "vibe": "Classic and cute", "emoji": "👜"},
    {"name": "Prada Re-Edition 2005", "brand": "Prada", "vibe": "Cool-girl staple", "emoji": "💫"},
    {"name": "Celine Triomphe", "brand": "Celine", "vibe": "Chic and timeless", "emoji": "🤎"},
    {"name": "Saint Laurent Le 5 à 7", "brand": "Saint Laurent", "vibe": "Effortlessly glamorous", "emoji": "🌙"},
    {"name": "Gucci Jackie 1961", "brand": "Gucci", "vibe": "Vintage sweetheart", "emoji": "💚"},
    {"name": "Hermès Kelly", "brand": "Hermès", "vibe": "Ultimate dream bag", "emoji": "👑"},
    {"name": "Loewe Puzzle Bag", "brand": "Loewe", "vibe": "Artsy luxury girl", "emoji": "🧩"},
    {"name": "Fendi Baguette", "brand": "Fendi", "vibe": "Playful It-girl", "emoji": "💛"},
]

JEWELLERY = [
    {"name": "Cartier Love Bracelet", "brand": "Cartier", "vibe": "Forever-love sparkle", "emoji": "💍"},
    {"name": "Van Cleef Alhambra Necklace", "brand": "Van Cleef & Arpels", "vibe": "Soft lucky charm", "emoji": "🍀"},
    {"name": "Tiffany HardWear Bracelet", "brand": "Tiffany & Co.", "vibe": "Bold and pretty", "emoji": "🩵"},
    {"name": "Bvlgari Serpenti Ring", "brand": "Bvlgari", "vibe": "Luxurious goddess energy", "emoji": "🐍"},
    {"name": "Cartier Juste un Clou", "brand": "Cartier", "vibe": "Edgy and iconic", "emoji": "🌹"},
    {"name": "Tiffany T Smile Necklace", "brand": "Tiffany & Co.", "vibe": "Sweet everyday shine", "emoji": "😊"},
    {"name": "Dior Rose des Vents Bracelet", "brand": "Dior", "vibe": "Delicate princess look", "emoji": "🌸"},
    {"name": "Chanel Coco Crush Ring", "brand": "Chanel", "vibe": "Minimal luxe", "emoji": "⭐"},
    {"name": "Van Cleef Sweet Alhambra Bracelet", "brand": "Van Cleef & Arpels", "vibe": "Tiny cute sparkle", "emoji": "🎀"},
    {"name": "Boucheron Quatre Ring", "brand": "Boucheron", "vibe": "Modern classy shine", "emoji": "💎"},
]

CUTE_SUGGESTIONS = [
    "Flowers 💐",
    "Perfume 🌷",
    "Skincare set 🫧",
    "Spa day 🛁",
    "Chocolate box 🍫",
    "Dinner date 🍝",
    "Weekend getaway ✈️",
    "Cute pajamas 🩷",
    "Silk scrunchies 🎀",
    "Lip gloss set 💄",
    "Polaroid camera 📸",
    "Plushie 🧸",
    "Matching bracelet 💞",
    "Coffee date ☕",
    "Handwritten love note 💌",
]

# -----------------------------
# Session state
# -----------------------------
if "wishlist" not in st.session_state:
    st.session_state.wishlist = [
        {"item": "Flowers 💐", "category": "Cute things", "priority": "Medium"},
        {"item": "Dinner date 🍝", "category": "Experiences", "priority": "High"},
    ]

if "last_result" not in st.session_state:
    st.session_state.last_result = None

# -----------------------------
# Styling
# -----------------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(180deg, #fff7fb 0%, #fffdf7 100%);
    }
    .main-title {
        text-align: center;
        font-size: 3rem;
        font-weight: 800;
        color: #ff4d8d;
        margin-bottom: 0.2rem;
    }
    .sub-title {
        text-align: center;
        font-size: 1.1rem;
        color: #8f5b75;
        margin-bottom: 1.5rem;
    }
    .cute-card {
        background: rgba(255,255,255,0.9);
        border: 2px solid #ffd6e7;
        border-radius: 22px;
        padding: 1rem 1.2rem;
        box-shadow: 0 8px 20px rgba(255, 105, 180, 0.08);
        margin-bottom: 1rem;
    }
    .result-box {
        background: linear-gradient(135deg, #fff0f7, #fff8e8);
        border: 2px solid #ffc7dd;
        border-radius: 24px;
        padding: 1.2rem;
        text-align: center;
        box-shadow: 0 12px 30px rgba(255, 105, 180, 0.12);
    }
    .tiny-note {
        color: #9a7188;
        font-size: 0.95rem;
    }
    .wishlist-pill {
        display: inline-block;
        padding: 0.25rem 0.6rem;
        border-radius: 999px;
        background: #ffe6f0;
        color: #a24c73;
        font-size: 0.85rem;
        margin-right: 0.35rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Helpers
# -----------------------------
def spin_roulette(pool, spin_seconds=2.0):
    """Fake spin animation for a cute roulette reveal."""
    placeholder = st.empty()
    steps = 18
    chosen = random.choice(pool)

    for i in range(steps):
        temp = random.choice(pool)
        placeholder.markdown(
            f"""
            <div class="result-box">
                <div style="font-size: 3rem;">🎡</div>
                <div style="font-size: 1.3rem; color:#b45a84;">Spinning for Rosa...</div>
                <div style="font-size: 1.8rem; font-weight:700; color:#ff4d8d; margin-top: 0.5rem;">
                    {temp["emoji"]} {temp["name"]}
                </div>
                <div style="color:#8a6a7b;">{temp["brand"]}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
        time.sleep(spin_seconds / steps)

    placeholder.empty()
    return chosen


def display_result(item, title):
    st.markdown(
        f"""
        <div class="result-box">
            <div style="font-size: 3rem;">{item["emoji"]}</div>
            <div style="font-size: 1rem; color:#b45a84; font-weight:700;">{title}</div>
            <div style="font-size: 1.8rem; font-weight:800; color:#ff4d8d; margin-top: 0.4rem;">
                {item["name"]}
            </div>
            <div style="font-size: 1rem; color:#8a6a7b; margin-top: 0.25rem;">
                {item["brand"]}
            </div>
            <div style="margin-top: 0.8rem; color:#7a6172;">
                {item["vibe"]}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def add_wishlist_item(item, category, priority):
    if item.strip():
        st.session_state.wishlist.append(
            {"item": item.strip(), "category": category, "priority": priority}
        )


# -----------------------------
# Header
# -----------------------------
st.markdown('<div class="main-title">Rosa\'s Dream Closet 💖</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="sub-title">A cute little Streamlit app with a luxury roulette and an adorable wishlist just for Rosa ✨</div>',
    unsafe_allow_html=True,
)

col_a, col_b, col_c = st.columns([1, 1, 1])
with col_a:
    st.metric("Dream Bags", len(BAGS))
with col_b:
    st.metric("Sparkly Jewellery", len(JEWELLERY))
with col_c:
    st.metric("Wishlist Items", len(st.session_state.wishlist))

tab1, tab2, tab3 = st.tabs(["🎡 Luxury Roulette", "🎀 Rosa's Wishlist", "💌 Little Extras"])

# -----------------------------
# Tab 1: Roulette
# -----------------------------
with tab1:
    left, right = st.columns([1.1, 0.9])

    with left:
        st.markdown('<div class="cute-card">', unsafe_allow_html=True)
        st.subheader("Spin the luxury roulette")
        st.write("Pick a category and let fate choose something dreamy for Rosa.")

        roulette_mode = st.radio(
            "Choose a roulette",
            ["Designer Bags", "Jewellery", "Mixed"],
            horizontal=True,
        )

        if roulette_mode == "Designer Bags":
            pool = BAGS
            spin_title = "Rosa's bag pick"
        elif roulette_mode == "Jewellery":
            pool = JEWELLERY
            spin_title = "Rosa's jewellery pick"
        else:
            pool = BAGS + JEWELLERY
            spin_title = "Rosa's luxury surprise"

        spin_speed = st.slider("Spin duration", 1.0, 4.0, 2.2, 0.2)

        if st.button("Spin for Rosa 💕", use_container_width=True):
            result = spin_roulette(pool, spin_seconds=spin_speed)
            st.session_state.last_result = (result, spin_title)
            st.balloons()

        st.markdown('</div>', unsafe_allow_html=True)

        if st.session_state.last_result:
            result, spin_title = st.session_state.last_result
            display_result(result, spin_title)

            if st.button("Add result to wishlist 💗", use_container_width=True):
                category = "Designer Bags" if result in BAGS else "Jewellery"
                add_wishlist_item(result["name"], category, "High")
                st.success(f"Added {result['name']} to Rosa's wishlist ✨")

    with right:
        st.markdown('<div class="cute-card">', unsafe_allow_html=True)
        st.subheader("What's inside the roulette?")
        preview_choice = st.selectbox(
            "Preview a dreamy item",
            ["Pick one..."] + [f'{x["emoji"]} {x["name"]}' for x in (BAGS + JEWELLERY)],
        )

        if preview_choice != "Pick one...":
            selected_name = preview_choice.split(" ", 1)[1]
            selected = next(x for x in (BAGS + JEWELLERY) if x["name"] == selected_name)
            display_result(selected, "Preview")

        st.markdown(
            """
            <p class="tiny-note">
            Inspired by iconic luxury picks. You can edit the lists in the code to swap in Rosa's exact dream pieces.
            </p>
            """,
            unsafe_allow_html=True,
        )
        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Tab 2: Wishlist
# -----------------------------
with tab2:
    left, right = st.columns([1, 1])

    with left:
        st.markdown('<div class="cute-card">', unsafe_allow_html=True)
        st.subheader("Add something Rosa would love")

        with st.form("wishlist_form", clear_on_submit=True):
            item = st.text_input("Wishlist item", placeholder="e.g. Van Cleef bracelet, flowers, date night...")
            category = st.selectbox(
                "Category",
                ["Designer Bags", "Jewellery", "Cute things", "Beauty", "Experiences", "Fashion", "Other"],
            )
            priority = st.select_slider("Priority", options=["Low", "Medium", "High"], value="Medium")
            submitted = st.form_submit_button("Add to wishlist 💞", use_container_width=True)

            if submitted:
                if item.strip():
                    add_wishlist_item(item, category, priority)
                    st.success(f"Added '{item}' to Rosa's wishlist 🎀")
                else:
                    st.warning("Add a cute item first 💭")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown('<div class="cute-card">', unsafe_allow_html=True)
        st.subheader("Quick add cute ideas")
        suggestion_cols = st.columns(3)
        for idx, suggestion in enumerate(CUTE_SUGGESTIONS):
            with suggestion_cols[idx % 3]:
                if st.button(suggestion, key=f"sugg_{idx}", use_container_width=True):
                    add_wishlist_item(suggestion, "Cute things", "Medium")
                    st.success(f"Added {suggestion} ✨")
        st.markdown('</div>', unsafe_allow_html=True)

    with right:
        st.markdown('<div class="cute-card">', unsafe_allow_html=True)
        st.subheader("Rosa's current wishlist")

        if not st.session_state.wishlist:
            st.info("The wishlist is empty for now. Time to add something adorable 💕")
        else:
            for idx, entry in enumerate(list(st.session_state.wishlist)):
                card_col, action_col = st.columns([5, 1])
                with card_col:
                    st.markdown(
                        f"""
                        <div style="background:#fffafb; border:1px solid #ffdbe9; border-radius:18px; padding:0.9rem 1rem; margin-bottom:0.6rem;">
                            <div style="font-size:1.05rem; font-weight:700; color:#d14f87;">{entry["item"]}</div>
                            <div style="margin-top:0.35rem;">
                                <span class="wishlist-pill">{entry["category"]}</span>
                                <span class="wishlist-pill">Priority: {entry["priority"]}</span>
                            </div>
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )
                with action_col:
                    if st.button("🗑️", key=f"del_{idx}"):
                        st.session_state.wishlist.pop(idx)
                        st.rerun()

        st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# Tab 3: Extras
# -----------------------------
with tab3:
    c1, c2 = st.columns([1, 1])

    with c1:
        st.markdown('<div class="cute-card">', unsafe_allow_html=True)
        st.subheader("Today's love note")
        notes = [
            "Rosa deserves something beautiful today 🌷",
            "A little sparkle for the prettiest girl ✨",
            "Luxury roulette says: spoil Rosa immediately 💖",
            "Reminder: cute gifts and quality time both count 💌",
            "Rosa is the real treasure, the gifts are just bonus points 👑",
        ]
        st.success(random.choice(notes))
        st.markdown('</div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="cute-card">', unsafe_allow_html=True)
        st.subheader("Wishlist summary")
        bag_count = sum(1 for x in st.session_state.wishlist if x["category"] == "Designer Bags")
        jewel_count = sum(1 for x in st.session_state.wishlist if x["category"] == "Jewellery")
        exp_count = sum(1 for x in st.session_state.wishlist if x["category"] == "Experiences")

        st.write(f"**Designer bags:** {bag_count}")
        st.write(f"**Jewellery:** {jewel_count}")
        st.write(f"**Experiences:** {exp_count}")
        st.write(f"**Last updated:** {datetime.now().strftime('%d %b %Y, %I:%M %p')}")
        st.markdown('</div>', unsafe_allow_html=True)

st.caption("Made with love for Rosa 💕")
