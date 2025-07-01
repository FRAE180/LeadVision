import streamlit as st

# -------------------------------
# Erweiterte Analysefunktion
# -------------------------------

def perform_web_analysis(company_name, region, language):
    # Platzhalter für echte Webanalyse, Artikelanalyse, Kundenverhalten etc.
    if company_name.lower() == "fensterkraftwerk":
        return {
            "summary": f"{company_name} ist ein innovatives Unternehmen im Bereich urbane Solartechnologie mit Sitz in {region}.",
            "profile": {
                "📍 Standort": "Berlin, Deutschland",
                "📅 Gründung": "ca. 2022–2023",
                "👥 Mitarbeiterzahl": "Kleines Team (Startup-Charakter)",
                "🎯 Fokus": "Plug-and-Play-Solarlösungen für Fensterbänke",
                "🔧 Technologien": "Solarmodule, Wechselrichter, Energiemessung",
                "💰 Finanzierung": "Crowdfunding (Kickstarter), keine VC-Finanzierung bekannt"
            },
            "scores_text": {
                "📏 Größe & Reifegrad": "🌱 Junges Startup mit DIY-Ursprung",
                "💡 Innovationsgrad": "🚀 Hoher Innovationsgrad durch kreative Nutzung urbaner Flächen",
                "🤝 Partnerschaften": "🤔 Keine bekannten Industrie- oder Technologiepartner",
                "🛠️ Engineering-Fokus": "🔧 Modular, einfach, DIY-freundlich",
                "🛒 Kundenverhalten": "🏙️ Zielgruppe: Mieter in Städten, preissensibel, umweltbewusst",
                "📦 Produkte & Projekte": "📈 Fensterkraftwerke, Upgrade-Sets, Kombinierboxen"
            },
            "numeric_scores": {
                "size_score": 4,
                "innovation_score": 8,
                "partnership_score": 3,
                "engineering_score": 7,
                "ebv_relevance_score": 9
            },
            "ebv_suggestions": [
                "Integration smarter Wechselrichter mit Energiemessung",
                "Einsatz von Sensorik zur Stromüberwachung",
                "Embedded Systems für Smart-Home-Anbindung",
                "Design-In-Support für modulare Energieprodukte",
                "Skalierung durch Industrialisierung & Supply Chain"
            ],
            "articles": [
                "Fensterkraftwerk revolutioniert urbane Solarnutzung – Artikel auf energiezukunft.eu",
                "Kickstarter-Kampagne erfolgreich abgeschlossen – Bericht auf startnext.com"
            ]
        }
    else:
        return {
            "summary": f"{company_name} ist ein innovatives Unternehmen mit Sitz in {region}.",
            "profile": {
                "📍 Standort": f"{region}",
                "📅 Gründung": "Nicht öffentlich bekannt",
                "👥 Mitarbeiterzahl": "Keine Angabe",
                "🎯 Fokus": "Technologieunternehmen",
                "🔧 Technologien": "Nicht spezifiziert",
                "💰 Finanzierung": "Keine Informationen verfügbar"
            },
            "scores_text": {
                "📏 Größe & Reifegrad": "📊 Eingeschätzt als kleines bis mittleres Unternehmen",
                "💡 Innovationsgrad": "💡 Innovationspotenzial vorhanden",
                "🤝 Partnerschaften": "🔍 Keine öffentlich bekannten Partnerschaften",
                "🛠️ Engineering-Fokus": "⚙️ Technologischer Fokus vermutet",
                "🛒 Kundenverhalten": "📉 Keine Daten verfügbar",
                "📦 Produkte & Projekte": "📦 Informationen nicht verfügbar"
            },
            "numeric_scores": {
                "size_score": 5,
                "innovation_score": 5,
                "partnership_score": 4,
                "engineering_score": 5,
                "ebv_relevance_score": 5
            },
            "ebv_suggestions": [
                "Analyse potenzieller Embedded-Systeme",
                "Sensorikbedarf prüfen",
                "Partnerschaften im Bereich Energieeffizienz"
            ],
            "articles": [
                "Keine spezifischen Artikel gefunden"
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
st.sidebar.header("⚖️ Kriteriengewichtung (0–10)")
weight_size = st.sidebar.slider("📏 Größe & Relevanz", 0, 10, 5)
weight_innovation = st.sidebar.slider("💡 Innovationspotenzial", 0, 10, 5)
weight_partnership = st.sidebar.slider("🤝 Partnerschaften", 0, 10, 5)
weight_engineering = st.sidebar.slider("🛠️ Engineering-Fokus", 0, 10, 5)
weight_ebv = st.sidebar.slider("🔍 EBV-Relevanz", 0, 10, 5)

# Trigger Analysis
if st.sidebar.button("🚀 Analyse starten"):
    result = perform_web_analysis(company_name, region, language)

    st.subheader(f"📄 Zusammenfassung: {company_name}")
    st.write(result["summary"])

    st.markdown("### 🏢 Firmenprofil")
    for key, value in result["profile"].items():
        st.write(f"- {key}: {value}")

    st.markdown("### 📊 Bewertung nach Kriterien")
    for key, value in result["scores_text"].items():
        st.write(f"- {key}: {value}")

    st.markdown("### 📈 Numerische Bewertung (0–10)")
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.metric("📏 Größe", result["numeric_scores"]["size_score"])
    col2.metric("💡 Innovation", result["numeric_scores"]["innovation_score"])
    col3.metric("🤝 Partnerschaften", result["numeric_scores"]["partnership_score"])
    col4.metric("🛠️ Engineering", result["numeric_scores"]["engineering_score"])
    col5.metric("🔍 EBV-Relevanz", result["numeric_scores"]["ebv_relevance_score"])

    # Gesamtbewertung berechnen
    total_score = (
        result["numeric_scores"]["size_score"] * weight_size +
        result["numeric_scores"]["innovation_score"] * weight_innovation +
        result["numeric_scores"]["partnership_score"] * weight_partnership +
        result["numeric_scores"]["engineering_score"] * weight_engineering +
        result["numeric_scores"]["ebv_relevance_score"] * weight_ebv
    ) / max(1, (weight_size + weight_innovation + weight_partnership + weight_engineering + weight_ebv))

    st.markdown("### 🧮 Gesamtbewertung")
    st.success(f"📊 Gesamtscore: {round(total_score, 2)} von 10")

    st.markdown("### 📰 Artikel & Quellen")
    for article in result["articles"]:
        st.write(f"- {article}")

    st.markdown("### 💡 Vorschläge für EBV Elektronik")
    for suggestion in result["ebv_suggestions"]:
        st.write(f"✅ {suggestion}")
else:
    st.info("Bitte gib die Firmendaten ein und starte die Analyse über die Seitenleiste.")
