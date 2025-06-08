# 📋 Smart-Home-App — v1.1.0 Milestone Tasks

This release focuses on expanding the functionality of the Settings screen, improving visual design, and making the app adapt cleanly to different screen sizes.

---

## ✅ General Goals
- [ ] Create a responsive, scalable layout
- [ ] Ensure UI works cleanly on both Pi touchscreen and larger displays
- [ ] Improve overall spacing, padding, font hierarchy

---

## ⚙️ Settings Screen Enhancements
- [ ] Add interactive theme picker (dropdown or radio buttons)
- [ ] Save selected theme to memory (local or via config file)
- [ ] Add system status/info section (optional: clock, hostname, IP)
- [ ] Improve layout consistency with other screens

---

## 🎨 Visual/Design Cleanup
- [ ] Use `dp`, `sp`, and `size_hint` consistently across all `.kv` files
- [ ] Replace fixed dimensions with dynamic sizing (`size_hint`, `pos_hint`)
- [ ] Unify margins and spacing between elements (especially in boxes/lists)

---

## 🧪 Testing & Responsiveness
- [ ] Test on Raspberry Pi touchscreen (7" / 800x480)
- [ ] Test on 1080p desktop environment
- [ ] Add mock resolutions for common screens and verify layout integrity

---

## 🧹 Technical Cleanup
- [ ] Remove unused imports or layout blocks
- [ ] Organize `main.py` logic into helpers if needed
- [ ] Ensure all `.kv` files are loaded conditionally and cleanly
