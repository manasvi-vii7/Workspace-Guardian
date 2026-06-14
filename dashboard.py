import streamlit as st

st.set_page_config(
    page_title="Workspace Guardian",
    page_icon="🛡️",
    layout="wide"
)
st.caption("AI-powered workspace monitoring and productivity assistant.")
st.title("🛡️ Workspace Guardian")

st.write("Real-time workspace monitoring dashboard")

import pandas as pd

df = pd.read_csv(
    "src/logs/activity.csv",
    header=None,
    names=[
        "timestamp",
        "objects",
        "risk",
        "focus_score",
        "state",
        "verdict"
    ]
)

latest = df.iloc[-1]

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "Focus Score",
        latest["focus_score"]
    )

with col2:
    st.metric(
        "Risk Level",
        latest["risk"]
    )

with col3:
    st.metric(
        "Objects Seen",
        len(str(latest["objects"]).split(","))
    )

st.subheader("📋 Recent Activity")

st.dataframe(
    df.tail(20),
    use_container_width=True
)

st.subheader("📈 Focus Score Trend")

st.line_chart(
    df["focus_score"]
)

risk_counts = df["risk"].value_counts()

# fetching state from risk level

risk = latest["risk"]

state = latest["state"]

verdict = latest["verdict"]

st.subheader("🛡 Guardian Analysis")

st.success(state)

st.write(verdict)

#Risk chart   

st.subheader("⚠️ Risk Distribution")

st.bar_chart(risk_counts)

with st.sidebar:

    st.header("Guardian Status")

    st.success("System Online")

    st.write(f"Entries Logged: {len(df)}")

st.sidebar.progress(
    int(latest["focus_score"])
)    

scores = df["focus_score"].tail(5)

#FOCUS TREND (Graphical)

if len(scores) >= 2:

    if scores.iloc[-1] > scores.mean():
        trend = "Improving 📈"

    elif scores.iloc[-1] < scores.mean():
        trend = "Declining 📉"

    else:
        trend = "Stable ➡️"

st.metric("Focus Trend", trend)      

#Session stats
avg_focus = round(df["focus_score"].mean(), 1)

highest_focus = df["focus_score"].max()

lowest_focus = df["focus_score"].min()

most_common_risk = df["risk"].mode()[0]

#Guardian personality

guardian_messages = {

    "Deep Focus":
        "Guardian approves. Stay locked in.",

    "Phone Usage Detected":
        "Phone spotted again. Stay focused.",

    "Workspace Unattended":
        "Workspace currently inactive.",

    "Minor Distraction":
        "Guardian notices minor distractions."
}

message = guardian_messages.get(state)
st.info(message)


st.caption ("Built with YOLOv8, OpenCV and Streamlit")

