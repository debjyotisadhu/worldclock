import streamlit as st
from datetime import datetime
from zoneinfo import ZoneInfo

# Page Config
st.set_page_config(page_title="Analog World Clock", layout="wide")

st.title("🕰️ World Clock")

# Timezones
timezones = {
    "California 🇺🇸": "America/Los_Angeles",
    "New York 🇺🇸": "America/New_York",
    "London 🇬🇧": "Europe/London",
    "Bangalore 🇮🇳": "Asia/Kolkata",
    "Singapore 🇸🇬": "Asia/Singapore",
}

#  CSS
clock_css = """
<style>
.clock {
    width: 180px;
    height: 180px;
    border: 6px solid #333;
    border-radius: 50%;
    position: relative;
    margin: auto;
}

.hand {
    position: absolute;
    bottom: 50%;
    left: 50%;
    transform-origin: bottom;
    transform: translateX(-50%) rotate(0deg);
    border-radius: 4px;
}

.hour {
    height: 45px;
    width: 6px;
    background: #333;
}

.minute {
    height: 65px;
    width: 4px;
    background: #555;
}

.second {
    height: 75px;
    width: 2px;
    background: red;
}

.center {
    width: 10px;
    height: 10px;
    background: #333;
    border-radius: 50%;
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
}

.label {
    text-align: center;
    margin-top: 10px;
    font-weight: 800;
}
</style>
"""

st.markdown(clock_css, unsafe_allow_html=True)

#  Layout
cols = st.columns(len(timezones))

now_utc = datetime.now(ZoneInfo("UTC"))

# Render Clocks
for col, (city, tz) in zip(cols, timezones.items()):
    local = now_utc.astimezone(ZoneInfo(tz))

    hour = local.hour % 12
    minute = local.minute
    second = local.second

    hour_deg = (hour + minute / 60) * 30
    minute_deg = minute * 6
    second_deg = second * 6

    clock_html = f"""
    <div class="clock">
        <div class="hand hour" style="transform: translateX(-50%) rotate({hour_deg}deg);"></div>
        <div class="hand minute" style="transform: translateX(-50%) rotate({minute_deg}deg);"></div>
        <div class="hand second" style="transform: translateX(-50%) rotate({second_deg}deg);"></div>
        <div class="center"></div>
    </div>
    <div class="label">{city}<br>{local.strftime('%H:%M:%S')}</div>
    """

    with col:
        st.markdown(clock_html, unsafe_allow_html=True)

st.markdown("---")
st.subheader("Important Links")
col1, col2, col3 = st.columns(3)
with col1 :
    st.link_button("Fix My PDF", "https://fixmypdf.streamlit.app/")


# Auto Refresh (Optional)
from streamlit_autorefresh import st_autorefresh
st_autorefresh(interval=1000)
