import streamlit as st
from config.export_utils import PDFReport


def render_export_section():
    with st.expander("📄 Export Final Report", expanded=True):
        if not st.session_state.get("summaries"):
            st.warning("No summaries available to export.")
            return

        # Ensure report object exists
        if "report" not in st.session_state:
            st.session_state.report = PDFReport()

        if st.button("📥 Generate PDF Report"):
            with st.spinner("Compiling report..."):
                st.session_state.report.clear()

                summaries = st.session_state.get("summaries", {})
                relevance_results = st.session_state.get("relevance_results", {})

                for fname, summary in summaries.items():
                    relevance = relevance_results.get(fname, "")
                    st.session_state.report.add_pdf_summary(
                        fname, summary, relevance
                    )

                file_path = st.session_state.report.save("Final_Report.pdf")

                with open(file_path, "rb") as f:
                    st.download_button(
                        "⬇️ Download Final Report",
                        f,
                        file_name="Final_Report.pdf",
                        mime="application/pdf"
                    )

    # Global clear button (outside expander for clarity)
    if st.button("🗑️ Clear All"):
        st.session_state["summaries"] = {}
        st.session_state["relevance_results"] = {}
        st.session_state.pop("report", None)

        st.success("All files and results cleared!")
        st.rerun()
