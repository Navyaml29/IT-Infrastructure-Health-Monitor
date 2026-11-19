import streamlit as st
import psutil
import platform
from datetime import datetime


st.set_page_config(
    page_title="IT Infrastructure Monitor",
    page_icon="🖥️",
    layout="wide"
)


CPU_LIMIT = 80
MEMORY_LIMIT = 80
DISK_LIMIT = 80


st.title("IT Infrastructure Health Monitoring System")
st.write("A simple dashboard to monitor system performance.")

st.divider()


st.subheader("System Information")

col1, col2, col3 = st.columns(3)

with col1:
    st.write("Operating System")
    st.info(platform.system())

with col2:
    st.write("System Architecture")
    st.info(platform.machine())

with col3:
    st.write("Processor")
    st.info(platform.processor() or "Not available")

st.divider()


def collect_system_data():

    cpu_usage = psutil.cpu_percent(interval=1)

    memory = psutil.virtual_memory()

    disk = psutil.disk_usage("/")

    return cpu_usage, memory, disk



if st.button("Refresh System Data"):

    st.rerun()



cpu, memory, disk = collect_system_data()


st.subheader("System Performance")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("CPU Utilization", f"{cpu}%")
    st.progress(int(cpu))

with col2:
    st.metric("Memory Utilization", f"{memory.percent}%")
    st.progress(int(memory.percent))

with col3:
    st.metric("Disk Utilization", f"{disk.percent}%")
    st.progress(int(disk.percent))

st.divider()

# Memory details
st.subheader("Memory Details")

col1, col2 = st.columns(2)

with col1:
    st.write(
        "Total Memory:",
        round(memory.total / (1024 ** 3), 2),
        "GB"
    )

    st.write(
        "Used Memory:",
        round(memory.used / (1024 ** 3), 2),
        "GB"
    )

with col2:
    st.write(
        "Available Memory:",
        round(memory.available / (1024 ** 3), 2),
        "GB"
    )

    st.write(
        "Memory Percentage:",
        f"{memory.percent}%"
    )

st.divider()

# Disk details
st.subheader("Disk Details")

st.write(
    "Total Disk Space:",
    round(disk.total / (1024 ** 3), 2),
    "GB"
)

st.write(
    "Used Disk Space:",
    round(disk.used / (1024 ** 3), 2),
    "GB"
)

st.write(
    "Free Disk Space:",
    round(disk.free / (1024 ** 3), 2),
    "GB"
)

st.divider()


st.subheader("Infrastructure Health Status")

if cpu >= CPU_LIMIT:
    st.error("Warning: CPU usage is high.")
else:
    st.success("CPU usage is normal.")

if memory.percent >= MEMORY_LIMIT:
    st.error("Warning: Memory usage is high.")
else:
    st.success("Memory usage is normal.")

if disk.percent >= DISK_LIMIT:
    st.error("Warning: Disk usage is high.")
else:
    st.success("Disk usage is normal.")

st.divider()


current_time = datetime.now()

st.caption(
    "Last Updated: " +
    current_time.strftime("%d-%m-%Y %H:%M:%S")
)

st.caption("Developed by Navya M L")