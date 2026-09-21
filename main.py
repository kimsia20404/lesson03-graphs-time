# ==================================================
# 그래프 4. 영화별 일관객 합계 TOP 10
# ==================================================

st.divider()

st.header("4. 영화별 일관객 합계 TOP 10")

st.write(
    "이 기간 동안 각 영화의 일관객을 모두 더해 "
    "관객이 가장 많았던 영화 10편을 비교합니다."
)

# 영화별 일관객 합계
movie_total = (
    df.groupby("영화명")
    .agg(
        일관객합계=("일관객", "sum"),
        상영일수=("날짜", "nunique")
    )
    .reset_index()
)

# 일관객 합계 기준 TOP 10
top10_movies = (
    movie_total
    .sort_values("일관객합계", ascending=False)
    .head(10)
    .copy()
)

# 그래프에서 관객이 많은 영화가 위에 오도록
top10_movies = top10_movies.sort_values(
    "일관객합계",
    ascending=True
)

fig4 = px.bar(
    top10_movies,
    x="일관객합계",
    y="영화명",
    orientation="h",
    labels={
        "일관객합계": "기간 내 일관객 합계",
        "영화명": "영화"
    },
    title="영화별 일관객 합계 TOP 10"
)

# 마우스를 올렸을 때 일관객 합계 + 10위권 등장 일수 표시
fig4.update_traces(
    customdata=top10_movies[["상영일수"]].values,
    hovertemplate=(
        "영화: %{y}"
        "<br>일관객 합계: %{x:,}명"
        "<br>10위권에 든 날: %{customdata[0]}일"
        "<extra></extra>"
    )
)

fig4.update_layout(
    xaxis=dict(
        tickformat=","
    ),
    yaxis=dict(
        categoryorder="total ascending"
    )
)

st.plotly_chart(
    fig4,
    use_container_width=True
)

st.markdown("**이 그래프로 알 수 있는 것**")
st.caption(
    "이 기간 동안 누적해서 가장 많은 관객을 모은 영화와 각 영화가 10위권에 머문 기간을 함께 비교할 수 있습니다."
)
