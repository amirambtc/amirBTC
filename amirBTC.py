
import streamlit as st

def loan_simulator(
    btc_amount: float,
    btc_price_usd: float,
    loan_apr_percent: float,
    current_loan_usd: float,
    after_months: int,
    new_btc_price_usd: float,
    max_ltv: float = 0.7
):
    initial_collateral = btc_amount * btc_price_usd
    max_initial_loan = initial_collateral * max_ltv
    apr = loan_apr_percent / 100
    monthly_interest = apr / 12
    repay_amount = current_loan_usd * ((1 + monthly_interest) ** after_months)
    new_collateral = btc_amount * new_btc_price_usd
    max_new_loan = new_collateral * max_ltv
    available_new_loan = max_new_loan - current_loan_usd

    return {
        "ارزش اولیه وثیقه (دلار)": initial_collateral,
        "حداکثر وام اولیه قابل دریافت (دلار)": max_initial_loan,
        "مبلغ قابل بازپرداخت بعد از مدت مشخص (دلار)": repay_amount,
        "ارزش فعلی وثیقه با قیمت جدید (دلار)": new_collateral,
        "سقف وام‌گیری با قیمت جدید (دلار)": max_new_loan,
        "مبلغ قابل برداشت اضافه (دلار)": available_new_loan
    }

st.set_page_config(page_title="شبیه‌ساز وام BTC برای Aave", page_icon="💰")
st.title("🔍 شبیه‌ساز ساده وام‌گیری با بیت‌کوین (WBTC) در Aave")
st.markdown("با این ابزار می‌تونی خیلی راحت بفهمی چقدر وام می‌تونی بگیری و چقدر باید پس بدی!")

btc_amount = st.number_input("✅ چند عدد BTC داری؟", min_value=0.0, value=5.0, step=0.1)
btc_price_usd = st.number_input("💵 قیمت هر BTC موقع وثیقه‌گذاری؟", min_value=0.0, value=20000.0, step=100.0)
loan_apr_percent = st.slider("📈 نرخ بهره سالانه وام (APR)?", 0.0, 20.0, 5.0)
current_loan_usd = st.number_input("💳 چه مقدار وام گرفتی؟ (دلار)", min_value=0.0, value=70000.0, step=100.0)
after_months = st.slider("📆 چند ماه گذشته از وام؟", 1, 36, 12)
new_btc_price_usd = st.number_input("📊 قیمت فعلی هر BTC؟", min_value=0.0, value=40000.0, step=100.0)

if st.button("🔍 محاسبه کن!"):
    result = loan_simulator(
        btc_amount,
        btc_price_usd,
        loan_apr_percent,
        current_loan_usd,
        after_months,
        new_btc_price_usd
    )

    st.success("✅ نتیجه محاسبات:")
    for key, value in result.items():
        st.write(f"**{key}:** ${value:,.2f}")

st.markdown("---")
st.caption("ساخته‌شده با ❤️ برای آموزش ساده DeFi")
