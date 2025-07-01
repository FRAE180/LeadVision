import streamlit as st

# -------------------------------
# Placeholder functions for logic
# -------------------------------

def perform_web_analysis(company_name, region, language):
    # Placeholder für echte Analyse (Scraping, NLP etc.)
    return {
        "summary": f"{company_name} ist ein innovatives Unternehmen im Bereich urbane Solartechnologie mit Sitz in {region}.",
        "size_score": 3,
        "innovation_score": 4,
        "partnership_score": 2,
        "engineering_score": 4,
        "ebv_relevance_score": 5,
        "ebv_suggestions": [
            "Integration smarter Wechselrichter mit Energiemessung",
            "Einsatz von Sensorik zur Stromüberwachung",
            "Embedded Systems für Smart-Home-Anbindung"
        ]
    }

# -------------------------------
# Streamlit App Layout
# -------------------------------

st.set_page_config(page_title="Kundenanalyse Tool", layout="wide")

st.title("🔍 Kundenanalyse Dashboard für EBV Elektronik")

# Sidebar Inputs
st.sidebar.header("📥 Eingabemaske")
company_name = st.sidebar.text_input("Firmenname", value="Fensterkraftwerk")
region = st.sidebar.text_input("Region", value="Berlin")
language = st.sidebar.selectbox("Sprache", ["Deutsch", "Englisch"])

st.sidebar.markdown("---")
st.sidebar.header("⚖️ Kriteriengewichtung (1–5)")
weight_size = st.sidebar.slider("📏 Größe & Relevanz", 1, 5, 3)
weight_innovation = st.sidebar.slider("💡 Innovationspotenzial", 1, 5, 3)
weight_partnership = st.sidebar.slider("🤝 Partnerschaften", 1, 5, 3)
weight_engineering = st.sidebar.slider("🛠️ Engineering-Fokus", 1, 5, 3)
weight_ebv = st.sidebar.slider("🔍 EBV-Relevanz", 1, 5, 3)

# Trigger Analysis
if st.sidebar.button("🚀 Analyse starten"):
    result = perform_web_analysis(company_name, region, language)

    st.subheader(f"📄 Zusammenfassung: {company_name}")
    st.write(result["summary"])

    st.markdown("### 📊 Bewertung")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("📏 Größe", result["size_score"])
    col2.metric("💡 Innovation", result["innovation_score"])
    col3.metric("🤝 Partnerschaften", result["partnership_score"])
    col4.metric("🛠️ Engineering", result["engineering_score"])
    col5.metric("🔍 EBV-Relevanz", result["ebv_relevance_score"])

    # Gesamtbewertung berechnen
    total_score = (
        result["size_score"] * weight_size +
        result["innovation_score"] * weight_innovation +
        result["partnership_score"] * weight_partnership +
        result["engineering_score"] * weight_engineering +
        result["ebv_relevance_score"] * weight_ebv
    ) / (weight_size + weight_innovation + weight_partnership + weight_engineering + weight_ebv)

    st.markdown("### 🧮 Gesamtbewertung")
    st.success(f"📈 Gesamtscore: {round(total_score, 2)} von 5")

    st.markdown("### 💡 Vorschläge für EBV Elektronik")
    for suggestion in result["ebv_suggestions"]:
        st.write(f"✅ {suggestion}")
else:
    st.info("Bitte gib die Firmendaten ein und starte die Analyse über die Seitenleiste.")
