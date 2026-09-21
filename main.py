# ==================================================
# 그래프 3. 날짜별 10위권 일관객 합계
# ==================================================

st.divider()

st.header("3. 날짜별 10위권 일관객 합계")

st.write(
    "날짜별로 그날의 10위권 영화 일관객을 모두 합산해 "
    "전체적인 영화 관객 규모의 변화를 살펴봅니다."
)

# 날짜별 10위권 일관객 합계 계산
daily_audience = (
    df.groupby("날짜", as_index=False)["일관객"]
    .sum()
    .sort_values("날짜")
)

# 일관객 합계가 가장 큰 3일
top3_days = (
    daily_audience
    .nlargest(3, "일관객")
    .sort_values("날짜")
)

# 영역 그래프
fig3 = px.area(
    daily_audience,
    x="날짜",
    y="일관객",
    labels={
        "날짜": "날짜",
        "일관객": "10위권 일관객 합계"
    },
    title="날짜별 10위권 일관객 합계"
)

# 마우스를 올렸을 때 표시되는 정보
fig3.update_traces(
    hovertemplate=(
        "날짜: %{x|%Y-%m-%d}"
        "<br>10위권 일관객 합계: %{y:,}명"
        "<extra></extra>"
    )
)

# 상위 3일을 그래프 위에 표시
for _, row in top3_days.iterrows():
    fig3.add_annotation(
        x=row["날짜"],
        y=row["일관객"],
        text=f"{row['날짜']:%Y-%m-%d}<br>{row['일관객']:,}명",
        showarrow=True,
        arrowhead=2,
        ax=0,
        ay=-50
    )

fig3.update_layout(
    hovermode="x unified",
    xaxis=dict(
        tickformat="%Y-%m-%d"
    ),
    yaxis=dict(
        tickformat=","
    )
)

st.plotly_chart(
    fig3,
    use_container_width=True
)

st.markdown("**이 그래프로 알 수 있는 것**")
st.caption(
    "날짜별 영화 관객 규모의 전체적인 흐름과 관객이 특히 많이 몰린 날을 알 수 있습니다."
)
