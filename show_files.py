import os, glob
import pandas as pd

root = os.path.join(os.path.expanduser("~"), "Desktop","abcd", "IMU_Gesture_Data")
paths = glob.glob(os.path.join(root, "**", "*.csv"), recursive=True)

rows = []
for p in paths:
    df = pd.read_csv(p)
    label = df["label"].iloc[0] if "label" in df.columns else os.path.normpath(p).split(os.sep)[-3]
    sess  = df["session_id"].iloc[0] if "session_id" in df.columns else os.path.normpath(p).split(os.sep)[-2]
    rows.append((sess, label, len(df), os.path.basename(p)))

d = pd.DataFrame(rows, columns=["session","label","rows","file"])
print("\nFILES PER SESSION + LABEL:")
print(d.groupby(["session","label"]).size())

print("\nAVG ROWS PER FILE:")
print(d.groupby(["session","label"])["rows"].mean().round(1))

print("\nTOTAL FILES:", len(d))
