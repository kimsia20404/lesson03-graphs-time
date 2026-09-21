import streamlit as st
import pandas as pd
import plotly.express as px


# --------------------------------------------------
# 기본 설정
# --------------------------------------------------

st.set_page_config(
    page_title="영화 데이터 그래프 도감 1 - 시간",
    page_icon="🎬",
    layout="wide"
)

st.title("🎬 영화 데이터 그래프 도감 1 - 시간")
st.write("영화별 일관객 변화를 시간의 흐름에 따라 살펴봅니다.")


# --------------------------------------------------
# 데이터 불러오기
# --------------------------------------------------

DATA_URL = "https://raw.githubusercontent.com/greatsong/modudata/main/data/kobis_daily.csv"

df = pd.read_csv(DATA_URL)

# 날짜를 진짜 날짜형으로 변환
df["날짜"] = pd.to_datetime(df["날짜"].astype(str), format="%Y%m%d")

# 숫자형 열 변환
numeric_columns = ["순위", "영화코드", "일관객", "누적관객", "스크린수", "상영횟수"]

for column in numeric_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")

# 날짜순으로 정렬
df = df.sort_values(["날짜", "순위"])


# --------------------------------------------------
# 그래프 1. 영화별 일관객 변화
# --------------------------------------------------

st.header("1. 영화별 일관객 변화")

st.write(
    "영화를 하나 선택하면 해당 영화의 날짜별 일관객 변화를 볼 수 있습니다."
)

movie_list = sorted(df["영화명"].dropna().unique())

selected_movie = st.selectbox(
    "영화를 선택하세요.",
    movie_list
)

movie_df = df[df["영화명"] == selected_movie].sort_values("날짜")

fig = px.line(
    movie_df,
    x="날짜",
    y="일관객",
    markers=True,
    labels={
        "날짜": "날짜",
        "일관객": "일관객 수"
    },
    title=f"「{selected_movie}」 날짜별 일관객 변화"
)

fig.update_traces(
    hovertemplate="날짜: %{x|%Y-%m-%d}<br>일관객: %{y:,}명<extra></extra>"
)

fig.update_layout(
    hovermode="x unified",
    xaxis=dict(
        tickformat="%Y-%m-%d"
    ),
    yaxis=dict(
        tickformat=","
    )
)

st.plotly_chart(fig, use_container_width=True)

st.markdown("**이 그래프로 알 수 있는 것**")
st.caption(
    "영화가 날짜에 따라 얼마나 많은 관객을 모았는지와 관객 수의 증가·감소 추이를 알 수 있습니다."
)


# --------------------------------------------------
# 앞으로 추가할 그래프 영역
# --------------------------------------------------

st.divider()

st.header("2. 다음 그래프")

st.info("앞으로 시간에 관한 새로운 그래프를 이곳에 추가합니다.")


st.divider()

st.header("3. 다음 그래프")

st.info("앞으로 새로운 그래프를 이곳에 추가합니다.")
