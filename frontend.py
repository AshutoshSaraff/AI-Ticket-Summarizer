import streamlit as st
from ticket_processer import TicketProcessor

# -------------------------
# Page Config
# -------------------------

st.set_page_config(
    page_title="AI Ticket Intelligence System",
    page_icon="🎫",
    layout="wide"
)

processor = TicketProcessor()

# -------------------------
# Header
# -------------------------

st.title("🎫 AI Ticket Intelligence System")

st.markdown("""
Analyze support tickets and automatically generate:

- 📄 Issue Summary
- 🔥 Priority Classification
- 📂 Issue Category
- 🖥 Impacted Platform
- 🔍 Recommended Investigation Steps
""")

st.divider()

# -------------------------
# Ticket Input
# -------------------------

ticket = st.text_area(
    "Enter Support Ticket",
    height=250,
    placeholder="""
Example:

Users are unable to log in after the latest update.
Several Android devices are stuck during OS upgrades.
Can you investigate the issue and suggest next steps?
"""
)

# -------------------------
# Analyze Button
# -------------------------

if st.button("🚀 Analyze Ticket", use_container_width=True):

    if not ticket.strip():

        st.warning("Please enter a support ticket.")

    else:

        with st.spinner("🤖 AI is analyzing the ticket..."):

            result = processor.process_ticket(ticket)

            print(type(result))
            print(result)

        if result:

            st.success("✅ Analysis Complete")

            st.divider()

            # -------------------------
            # Summary
            # -------------------------

            st.subheader("📄 Summary")

            st.info(
                result["summary"]
            )

            st.divider()

            # -------------------------
            # Priority / Category / Platform
            # -------------------------

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    label="🔥 Priority",
                    value=result["priority"]
                )

            with col2:

                st.write("### 📂 Category")

                st.success(
                    result["category"]
                )

            with col3:

                st.write("### 🖥 Platform")

                st.info(
                    result["platform"]
                )

            st.divider()

            # -------------------------
            # Next Investigation Steps
            # -------------------------

            st.subheader(
                "🔍 Next Investigation Steps"
            )

            questions = result.get(
                "next_steps",
                []
            )

            if questions:

                for index, question in enumerate(
                    questions,
                    start=1
                ):

                    st.write(
                        f"{index}. {question}"
                    )

            else:

                st.write(
                    "No investigation steps generated."
                )

        else:

            st.error(
                "❌ AI Analysis Failed."
            )