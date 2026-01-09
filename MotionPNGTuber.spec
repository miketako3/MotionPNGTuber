# -*- mode: python ; coding: utf-8 -*-
import os

project_root = os.path.abspath(os.path.dirname(__file__))

script_files = [
    "auto_mouth_track_v2.py",
    "calibrate_mouth_track.py",
    "auto_erase_mouth.py",
    "face_track_anime_detector.py",
    "erase_mouth_offline.py",
    "loop_lipsync_runtime_patched_emotion_auto.py",
    "loop_lipsync_runtime_patched.py",
    "preview_mouth_track.py",
    "realtime_emotion_audio.py",
    "mouth_sprite_extractor.py",
    "mouth_erase_tuner_gui.py",
    "mouth_sprite_extractor_gui.py",
]

datas = [
    (os.path.join(project_root, "assets"), "assets"),
    (os.path.join(project_root, "mouth_dir"), "mouth_dir"),
]

datas += [(os.path.join(project_root, f), ".") for f in script_files]

block_cipher = None


# Build single GUI executable that also supports --run-script.
analysis_scripts = [os.path.join(project_root, "mouth_track_gui.py")]
analysis_scripts += [os.path.join(project_root, f) for f in script_files]

a = Analysis(
    analysis_scripts,
    pathex=[project_root],
    binaries=[],
    datas=datas,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts[0],
    [],
    exclude_binaries=True,
    name="MotionPNGTuber",
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name="MotionPNGTuber",
)
