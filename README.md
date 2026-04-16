# [ PROJECT: CYTUS-II-MONONOTE ]

An automated research project focused on restructuring Cytus II rhythm data into a simplified "Single-Note" (MonoNote) format. This project utilizes Python automation and AssetBundle manipulation to explore game engine limits and chart synchronization.

---

## [ 01. DISCLAIMER ]

* [!] **NO ORIGINAL BINARIES:** This repository does NOT contain any original game binaries (.ipa/.apk), proprietary assets, or copyrighted music files belonging to **Rayark Inc.**
* [!] **RESEARCH ONLY:** This project is strictly for educational and research purposes.
* [!] **USER RESPONSIBILITY:** Users are solely responsible for their own game files. We do not encourage or support software piracy.
* [!] **TRADEMARKS:** All trademarks and copyrights belong to their respective owners.

---

## [ 02. CORE_FEATURES ]

+ [ AUTO_CONVERSION ] : Batch-processing scripts for JSON chart data.
+ [ MONO_LOGIC ] : Restructures complex `m_Script` fields into a single-note (MonoNote) flow.
+ [ BATCH_OPERATIONS ] : Automated tools for mass renaming and bundle integration.

---

## [ 03. TECH_SPECIFICATIONS ]

| COMPONENT | METHOD | TARGET |
| :--- | :--- | :--- |
| Chart Engine | JSON Schema Remapping | `TextAsset` |
| Automation | Python 3.x | File I/O |
| Extraction | UABEA / UABE | AssetBundles |

---

## [ 04. INSTALLATION ]

**This project has been fully updated and verified for version: v5.2.12**

To apply the modified charts, download the processed `.ab` files and replace them in the following directories based on your platform:

### > iOS (Jailbroken or Sideloaded)
`Path: CytusII.app/Data/Raw/AssetBundles`

### > Android
`Path: /Android/data/com.rayark.cytus2/files/AssetBundles`
*(Note: You may need a file manager with root/data access permissions to see this folder.)*

---

## [ 05. DEPLOYMENT_FLOW ]

1. Extract target `.ab` files using UABEA.
2. Export JSON/Text dumps for the desired assets.
3. Execute the Python automation suite:
   `python Scripts/batch_json_mod.py`
4. Re-import modified dumps and rebuild the AssetBundle.

---

## [ 06. LICENSE ]

[ CC BY-NC-SA 4.0 ]
>> Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International.

---

