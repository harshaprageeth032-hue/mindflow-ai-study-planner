import streamlit as st
import requests

API_BASE_URL = "http://127.0.0.1:8000/api"


st.set_page_config(
    page_title="MindFlow AI | Study & Task Architect",
    layout="wide",
    initial_sidebar_state="expanded"
)


st.markdown("""
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20,400,0,0" />

<style>
    .stApp {
        background-color: #0B0F19;
        font-family: 'Inter', sans-serif;
    }

    .icon-inline {
        font-family: 'Material Symbols Outlined';
        font-weight: normal;
        font-style: normal;
        font-size: 20px;
        line-height: 1;
        letter-spacing: normal;
        text-transform: none;
        display: inline-flex;
        align-items: center;
        vertical-align: middle;
        margin-right: 6px;
    }

    /* Hero Banner */
    .hero-banner {
        background: linear-gradient(135deg, #111827 0%, #1E293B 100%);
        border: 1px solid #1F2937;
        border-radius: 12px;
        padding: 24px 30px;
        margin-bottom: 24px;
        box-shadow: 0 4px 24px rgba(0, 0, 0, 0.4);
    }
    .hero-title {
        font-size: 24px;
        font-weight: 700;
        color: #F9FAFB;
        display: flex;
        align-items: center;
        gap: 10px;
        margin: 0;
    }
    .hero-subtitle {
        font-size: 14px;
        color: #9CA3AF;
        margin-top: 6px;
    }

    /* KPI Metric Cards */
    .metric-card {
        background-color: #111827;
        border: 1px solid #1F2937;
        border-radius: 10px;
        padding: 18px 20px;
    }
    .metric-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        color: #9CA3AF;
        font-size: 12px;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.6px;
    }
    .metric-value {
        font-size: 28px;
        font-weight: 700;
        color: #F3F4F6;
        margin-top: 8px;
    }

    /* Executive Summary Box */
    .summary-box {
        background-color: #111827;
        border-left: 3px solid #38BDF8;
        border-top: 1px solid #1F2937;
        border-right: 1px solid #1F2937;
        border-bottom: 1px solid #1F2937;
        padding: 14px 18px;
        border-radius: 0 8px 8px 0;
        color: #D1D5DB;
        font-size: 14px;
        line-height: 1.6;
        margin: 14px 0 18px 0;
    }
    .summary-label {
        color: #38BDF8;
        font-weight: 600;
        font-size: 12px;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        display: flex;
        align-items: center;
        margin-bottom: 6px;
    }

    /* Priority Badges */
    .badge-high {
        background-color: rgba(239, 68, 68, 0.12);
        color: #F87171;
        border: 1px solid rgba(239, 68, 68, 0.35);
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.3px;
    }
    .badge-medium {
        background-color: rgba(245, 158, 11, 0.12);
        color: #FBBF24;
        border: 1px solid rgba(245, 158, 11, 0.35);
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.3px;
    }
    .badge-low {
        background-color: rgba(16, 185, 129, 0.12);
        color: #34D399;
        border: 1px solid rgba(16, 185, 129, 0.35);
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 600;
        letter-spacing: 0.3px;
    }
    .time-pill {
        background-color: #1F2937;
        color: #9CA3AF;
        border: 1px solid #374151;
        padding: 3px 10px;
        border-radius: 6px;
        font-size: 11px;
        font-weight: 500;
        margin-left: 6px;
        display: inline-flex;
        align-items: center;
        gap: 4px;
    }

    /* Status Indicator */
    .status-badge {
        display: inline-flex;
        align-items: center;
        gap: 8px;
        font-size: 12px;
        font-weight: 500;
        color: #9CA3AF;
        background: #111827;
        padding: 6px 12px;
        border-radius: 6px;
        border: 1px solid #1F2937;
        width: 100%;
    }
    .dot-online {
        height: 8px;
        width: 8px;
        background-color: #10B981;
        border-radius: 50%;
        display: inline-block;
    }
    .dot-offline {
        height: 8px;
        width: 8px;
        background-color: #EF4444;
        border-radius: 50%;
        display: inline-block;
    }
</style>
""", unsafe_allow_html=True)


notes = []
api_online = True
try:
    response = requests.get(f"{API_BASE_URL}/notes")
    if response.status_code == 200:
        notes = response.json()
except requests.exceptions.ConnectionError:
    api_online = False


with st.sidebar:
    st.markdown("""
        <div style="display:flex; align-items:center; gap:8px; font-size:20px; font-weight:700; color:#F9FAFB;">
            <span class="material-symbols-outlined" style="color:#38BDF8; font-size:24px;">account_tree</span>
            MindFlow AI
        </div>
        <div style="font-size:12px; color:#9CA3AF; margin-top:2px;">Study & Engineering Workflow Architect</div>
    """, unsafe_allow_html=True)
    
    st.divider()
    
    st.markdown("""
        <div style="display:flex; align-items:center; font-size:14px; font-weight:600; color:#E5E7EB; margin-bottom:10px;">
            <span class="icon-inline" style="color:#38BDF8;">post_add</span> New Study Plan
        </div>
    """, unsafe_allow_html=True)

    with st.form("note_form", clear_on_submit=True):
        title = st.text_input("Topic / Module Title", placeholder="e.g., Microservices & Docker")
        raw_content = st.text_area(
            "Raw Notes or Task Dump",
            height=180,
            placeholder="Paste lecture notes, project requirements, or technical tasks..."
        )
        submitted = st.form_submit_button(
            "Generate AI Plan",
            icon=":material/auto_awesome:",
            use_container_width=True,
            type="primary"
        )

        if submitted:
            if not title.strip() or not raw_content.strip():
                st.warning("Please fill in both fields.")
            else:
                with st.spinner("Structuring workflow with Gemini AI..."):
                    res = requests.post(
                        f"{API_BASE_URL}/notes/analyze",
                        json={"title": title, "raw_content": raw_content}
                    )
                    if res.status_code == 200:
                        st.success("Plan created successfully.")
                        st.rerun()
                    else:
                        st.error(f"API Error: {res.text}")

    st.divider()
    priority_filter = st.selectbox("Filter Tasks by Priority", ["All", "High", "Medium", "Low"])
    
    st.markdown("<br>", unsafe_allow_html=True)
    if api_online:
        st.markdown('<div class="status-badge"><span class="dot-online"></span> FastAPI Service Online</div>', unsafe_allow_html=True)
    else:
        st.markdown('<div class="status-badge"><span class="dot-offline"></span> FastAPI Service Offline</div>', unsafe_allow_html=True)


st.markdown("""
<div class="hero-banner">
    <div class="hero-title">
        <span class="material-symbols-outlined" style="color:#38BDF8; font-size:28px;">layers</span>
        Study & Task Workspace
    </div>
    <div class="hero-subtitle">Transform unstructured technical notes into prioritized, time-boxed engineering workflows.</div>
</div>
""", unsafe_allow_html=True)

if not api_online:
    st.error("Cannot connect to FastAPI backend (http://127.0.0.1:8000). Please start the Uvicorn server.")
    st.stop()


total_plans = len(notes)
all_tasks = [t for n in notes for t in n["tasks"]]
total_tasks = len(all_tasks)
completed_tasks = sum(1 for t in all_tasks if t["is_completed"])
total_minutes = sum(t["estimated_minutes"] for t in all_tasks if not t["is_completed"])
completion_rate = int((completed_tasks / total_tasks) * 100) if total_tasks > 0 else 0


c1, c2, c3, c4 = st.columns(4)
with c1:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-header"><span>Active Modules</span><span class="material-symbols-outlined" style="color:#38BDF8;">folder_open</span></div>
            <div class="metric-value">{total_plans}</div>
        </div>
    """, unsafe_allow_html=True)
with c2:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-header"><span>Tasks Completed</span><span class="material-symbols-outlined" style="color:#10B981;">task_alt</span></div>
            <div class="metric-value">{completed_tasks}/{total_tasks}</div>
        </div>
    """, unsafe_allow_html=True)
with c3:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-header"><span>Completion Rate</span><span class="material-symbols-outlined" style="color:#818CF8;">analytics</span></div>
            <div class="metric-value">{completion_rate}%</div>
        </div>
    """, unsafe_allow_html=True)
with c4:
    st.markdown(f"""
        <div class="metric-card">
            <div class="metric-header"><span>Remaining Effort</span><span class="material-symbols-outlined" style="color:#F59E0B;">schedule</span></div>
            <div class="metric-value">{total_minutes}m</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if not notes:
    st.info("Use the sidebar panel on the left to submit your first note and generate a structured study plan.")
else:
    for note in notes:
        filtered_tasks = [
            t for t in note["tasks"]
            if priority_filter == "All" or t["priority"] == priority_filter
        ]
        if priority_filter != "All" and not filtered_tasks:
            continue

        note_total = len(note["tasks"])
        note_done = sum(1 for t in note["tasks"] if t["is_completed"])
        note_progress = (note_done / note_total) if note_total > 0 else 0

        with st.container(border=True):
            
            head_col1, head_col2 = st.columns([0.88, 0.12])
            with head_col1:
                st.markdown(f"""
                    <div style="display:flex; align-items:center; font-size:18px; font-weight:600; color:#F9FAFB; margin-bottom:8px;">
                        <span class="icon-inline" style="color:#38BDF8;">description</span> {note['title']}
                    </div>
                """, unsafe_allow_html=True)
            with head_col2:
                if st.button("Delete", icon=":material/delete:", key=f"del_{note['id']}", use_container_width=True):
                    requests.delete(f"{API_BASE_URL}/notes/{note['id']}")
                    st.rerun()

            
            st.progress(note_progress, text=f"Module Progress: {note_done} of {note_total} tasks completed")

            
            st.markdown(f"""
                <div class="summary-box">
                    <div class="summary-label"><span class="icon-inline" style="font-size:16px;">auto_awesome</span> Executive Summary</div>
                    {note["summary"]}
                </div>
            """, unsafe_allow_html=True)

            
            for task in filtered_tasks:
                t_col1, t_col2, t_col3 = st.columns([0.04, 0.71, 0.25])
                with t_col1:
                    checked = st.checkbox("done", value=task["is_completed"], key=f"chk_{task['id']}", label_visibility="collapsed")
                    if checked != task["is_completed"]:
                        requests.patch(f"{API_BASE_URL}/tasks/{task['id']}/toggle")
                        st.rerun()
                with t_col2:
                    if task["is_completed"]:
                        st.markdown(f"<span style='color:#6B7280; text-decoration:line-through; font-size:14px;'>{task['description']}</span>", unsafe_allow_html=True)
                    else:
                        st.markdown(f"<span style='color:#E5E7EB; font-weight:500; font-size:14px;'>{task['description']}</span>", unsafe_allow_html=True)
                with t_col3:
                    p = task["priority"]
                    badge_cls = "badge-high" if p == "High" else ("badge-medium" if p == "Medium" else "badge-low")
                    st.markdown(
                        f"<div style='text-align:right; display:flex; justify-content:flex-end; align-items:center;'>"
                        f"<span class='{badge_cls}'>{p.upper()}</span>"
                        f"<span class='time-pill'><span class='material-symbols-outlined' style='font-size:14px;'>schedule</span>{task['estimated_minutes']}m</span>"
                        f"</div>",
                        unsafe_allow_html=True
                    )
