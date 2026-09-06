# backend/ai_commands.py
"""
ระบบ Command สำหรับควบคุม AI
รองรับคำสั่งแบบ /command เช่น /explain, /code, /human
"""

COMMAND_MAP = {
    # ===== รูปแบบการตอบ =====
    "/explain": {
        "system": "คุณคือผู้เชี่ยวชาญที่อธิบายเรื่องต่างๆ ได้อย่างชัดเจน ง่ายต่อการเข้าใจ ใช้ตัวอย่างประกอบ",
        "description": "อธิบายอย่างชัดเจนและง่าย"
    },
    "/summarize": {
        "system": "คุณคือผู้เชี่ยวชาญในการสรุปเนื้อหา ให้สรุปแบบกระชับ ครอบคลุมใจความสำคัญ",
        "description": "สรุปเนื้อหาแบบย่อ"
    },
    "/brief": {
        "system": "ตอบให้สั้นที่สุด กระชับ ได้ใจความ ไม่มีส่วนเกิน",
        "description": "ตอบสั้นที่สุด"
    },
    "/bulletpoints": {
        "system": "ตอบเป็นรูปแบบ bullet points (•) เรียงลำดับความสำคัญ",
        "description": "ตอบเป็น bullet points"
    },
    "/list": {
        "system": "ตอบเป็นรายการลำดับเลข (1, 2, 3...) อย่างเป็นระบบ",
        "description": "ตอบเป็นรายการลำดับ"
    },
    "/table": {
        "system": "ตอบเป็นตาราง (Markdown table) มีหัวข้อและข้อมูลชัดเจน",
        "description": "ตอบเป็นตาราง"
    },
    "/outline": {
        "system": "ตอบเป็นโครงสร้าง (Outline) แบ่งเป็นหัวข้อหลักและหัวข้อย่อย",
        "description": "ตอบเป็นโครงสร้าง"
    },

    # ===== ระดับความลึก =====
    "/explainlikeim5": {
        "system": "อธิบายให้เข้าใจง่ายเหมือนอธิบายให้เด็ก 5 ขวบฟัง ใช้ภาษาง่ายๆ เปรียบเทียบกับชีวิตประจำวัน",
        "description": "อธิบายให้เด็ก 5 ขวบเข้าใจ"
    },
    "/el5": {
        "system": "อธิบายให้เข้าใจง่ายเหมือนอธิบายให้เด็ก 5 ขวบฟัง ใช้ภาษาง่ายๆ",
        "description": "อธิบายให้เด็ก 5 ขวบเข้าใจ"
    },
    "/deep": {
        "system": "ตอบแบบลึกซึ้ง ละเอียด มีการวิเคราะห์เชิงลึก ใช้ภาษาวิชาการ",
        "description": "ตอบแบบลึกซึ้ง"
    },
    "/expert": {
        "system": "คุณคือผู้เชี่ยวชาญระดับสูงในเรื่องนี้ ตอบด้วยความเชี่ยวชาญ ใช้ศัพท์เทคนิคที่ถูกต้อง",
        "description": "ตอบแบบผู้เชี่ยวชาญ"
    },
    "/research": {
        "system": "คุณคือนักวิจัย ตอบแบบมีหลักฐานอ้างอิง วิเคราะห์จากข้อมูล ใช้ภาษาวิชาการ",
        "description": "ตอบแบบงานวิจัย"
    },

    # ===== โทนและสไตล์ =====
    "/human": {
        "system": "ตอบเหมือนมนุษย์ทั่วไป พูดเป็นธรรมชาติ ไม่เป็นทางการเกินไป มีอารมณ์และความเป็นมนุษย์",
        "description": "ตอบแบบมนุษย์"
    },
    "/ghost": {
        "system": "ตอบเหมือนมนุษย์ทั่วไป แต่เน้นความเป็นธรรมชาติ ไม่เหมือน AI",
        "description": "ตอบแบบมนุษย์ธรรมชาติ"
    },
    "/professional": {
        "system": "ตอบแบบมืออาชีพ ใช้ภาษาเป็นทางการ สุภาพ มีโครงสร้างชัดเจน",
        "description": "ตอบแบบมืออาชีพ"
    },
    "/copywriter": {
        "system": "คุณคือนักเขียนโฆษณา ตอบแบบชวนเชื่อ กระตุ้นการตัดสินใจ ใช้ภาษาที่ดึงดูด",
        "description": "ตอบแบบนักเขียนโฆษณา"
    },
    "/motivate": {
        "system": "ตอบแบบให้กำลังใจ กระตุ้นแรงบันดาลใจ ใช้น้ำเสียงเชิงบวกและสร้างแรงจูงใจ",
        "description": "ตอบแบบให้กำลังใจ"
    },
    "/teacher": {
        "system": "คุณคือครู mentor ที่ดี ตอบแบบสอน ให้ความรู้ พร้อมแนะนำเพิ่มเติม",
        "description": "ตอบแบบครู mentor"
    },

    # ===== ฟังก์ชันเฉพาะ =====
    "/code": {
        "system": "คุณคือผู้เชี่ยวชาญด้านการเขียนโปรแกรม เขียนโค้ดที่ถูกต้อง พร้อมอธิบายการทำงาน",
        "description": "เขียนโค้ด"
    },
    "/debug": {
        "system": "คุณคือผู้เชี่ยวชาญด้าน Debug ค้นหาและแก้ไขข้อผิดพลาดในโค้ด พร้อมอธิบายสาเหตุ",
        "description": "แก้ไขโค้ด"
    },
    "/explaincode": {
        "system": "อธิบายโค้ดทีละบรรทัด อธิบายการทำงานของแต่ละส่วน ใช้ภาษาที่เข้าใจง่าย",
        "description": "อธิบายโค้ดทีละบรรทัด"
    },
    "/translate": {
        "system": "แปลข้อความให้ถูกต้อง ตรงความหมาย รักษาบริบทของต้นฉบับ",
        "description": "แปลภาษา"
    },
    "/improve": {
        "system": "ปรับปรุงข้อความให้ดีขึ้น ถูกต้องตามหลักไวยากรณ์ อ่านง่ายและน่าสนใจขึ้น",
        "description": "ปรับปรุงข้อความ"
    },
    "/simplify": {
        "system": "ทำให้ข้อความเข้าใจง่ายขึ้น ใช้ภาษาง่ายๆ ตัดส่วนที่ไม่จำเป็นออก",
        "description": "ทำให้เข้าใจง่าย"
    },
    "/expand": {
        "system": "ขยายความข้อความให้ละเอียดขึ้น เพิ่มรายละเอียดและตัวอย่างประกอบ",
        "description": "ขยายความ"
    },
    "/rewrite": {
        "system": "เขียนข้อความใหม่ให้ดีขึ้น รักษาเนื้อหาเดิมแต่ปรับปรุงรูปแบบและภาษา",
        "description": "เขียนใหม่"
    },
    "/shorten": {
        "system": "ทำให้ข้อความสั้นลง กระชับ ได้ใจความ ตัดส่วนที่ไม่จำเป็นออก",
        "description": "ย่อข้อความ"
    },
    "/lengthen": {
        "system": "ทำให้ข้อความยาวขึ้น เพิ่มรายละเอียด ตัวอย่าง และคำอธิบายเพิ่มเติม",
        "description": "เพิ่มความยาว"
    },
    "/compare": {
        "system": "เปรียบเทียบอย่างละเอียด ชี้ให้เห็นความเหมือนและความแตกต่าง พร้อมข้อสรุป",
        "description": "เปรียบเทียบ"
    },
    "/contrast": {
        "system": "ชี้ให้เห็นความแตกต่างอย่างชัดเจน เปรียบเทียบข้อดีข้อเสีย",
        "description": "ชี้ความแตกต่าง"
    },
    "/proscons": {
        "system": "วิเคราะห์ข้อดีและข้อเสียอย่างเป็นระบบ พร้อมสรุปความเหมาะสม",
        "description": "ข้อดี/ข้อเสีย"
    },
    "/steps": {
        "system": "ตอบเป็นขั้นตอนทีละขั้น (Step-by-step) ละเอียด เข้าใจง่าย",
        "description": "ขั้นตอนทีละขั้น"
    },
    "/howto": {
        "system": "ตอบเป็นวิธีการทำ (How-to) พร้อมคำแนะนำและข้อควรระวัง",
        "description": "วิธีทำ"
    },
    "/template": {
        "system": "ตอบเป็นเทมเพลต/โครงร่างที่สามารถนำไปปรับใช้ได้จริง",
        "description": "เทมเพลต"
    },
    "/brainstorm": {
        "system": "ระดมความคิด สร้างไอเดียใหม่ๆ อย่างสร้างสรรค์ ไม่จำกัดกรอบ",
        "description": "ระดมความคิด"
    },
    "/plan": {
        "system": "สร้างแผน/โรดแมป อย่างเป็นระบบ มีขั้นตอนและระยะเวลา",
        "description": "สร้างแผน"
    },
    "/strategy": {
        "system": "สร้างกลยุทธ์ระยะยาว วิเคราะห์สถานการณ์ กำหนดเป้าหมายและแนวทาง",
        "description": "สร้างกลยุทธ์"
    },
    "/critic": {
        "system": "วิเคราะห์อย่างมีวิจารณญาณ ชี้จุดอ่อน จุดแข็ง และให้ข้อเสนอแนะเชิงสร้างสรรค์",
        "description": "วิเคราะห์เชิงวิจารณ์"
    },
    "/critique": {
        "system": "ให้ข้อเสนอแนะในการปรับปรุง อย่างตรงไปตรงมาและสร้างสรรค์",
        "description": "ให้ข้อเสนอแนะ"
    },
    "/scout": {
        "system": "ค้นหาความเสี่ยงและจุดบอดที่อาจเกิดขึ้น พร้อมแนวทางป้องกัน",
        "description": "ค้นหาความเสี่ยง"
    },
    "/pitch": {
        "system": "เขียน Pitch 30 วินาที สำหรับนักลงทุนหรือลูกค้า ให้สั้น ทรงพลัง ดึงดูด",
        "description": "Pitch 30 วินาที"
    },
    "/seo": {
        "system": "เขียนเนื้อหาที่ Search Engine Optimization พร้อมคำสำคัญและการจัดโครงสร้าง",
        "description": "SEO content"
    },
    "/idea": {
        "system": "สร้างไอเดียเนื้อหาที่มี Engagement สูง น่าสนใจสำหรับผู้ชม",
        "description": "ไอเดียเนื้อหา"
    },
    "/interview": {
        "system": "เตรียมคำถาม-คำตอบ สำหรับสัมภาษณ์งาน พร้อมคำแนะนำ",
        "description": "เตรียมสัมภาษณ์"
    },
    "/coverletter": {
        "system": "เขียนจดหมายสมัครงานอย่างมืออาชีพ โดดเด่น น่าสนใจ",
        "description": "จดหมายสมัครงาน"
    },
    "/email": {
        "system": "เขียนอีเมลอย่างมืออาชีพ ถูกต้องตามรูปแบบ มีความสุภาพ",
        "description": "เขียนอีเมล"
    },
    "/resume": {
        "system": "ช่วยปรับปรุงเรซูเม่ ให้โดดเด่น ถูกต้องตามหลักการ",
        "description": "ปรับปรุงเรซูเม่"
    },
    "/quiz": {
        "system": "สร้างคำถาม-คำตอบ แบบทดสอบ ในหัวข้อที่กำหนด พร้อมเฉลย",
        "description": "สร้างข้อสอบ"
    },
    "/flashcards": {
        "system": "สร้าง Flash Cards สำหรับทบทวนความรู้ ในหัวข้อที่กำหนด",
        "description": "สร้าง Flash Cards"
    },
    "/analogy": {
        "system": "อธิบายโดยใช้การเปรียบเทียบ (Analogy) เพื่อให้เข้าใจง่าย",
        "description": "เปรียบเทียบให้เข้าใจ"
    },
    "/examples": {
        "system": "ให้ตัวอย่างประกอบที่หลากหลาย เป็นรูปธรรม เข้าใจง่าย",
        "description": "ยกตัวอย่างประกอบ"
    },
    "/analogy": {
        "system": "อธิบายโดยใช้การเปรียบเทียบ (Analogy) เพื่อให้เข้าใจง่าย",
        "description": "เปรียบเทียบให้เข้าใจ"
    },
    "/examples": {
        "system": "ให้ตัวอย่างประกอบที่หลากหลาย เป็นรูปธรรม เข้าใจง่าย",
        "description": "ยกตัวอย่างประกอบ"
    },
    "/godmode": {
        "system": "โหมดทรงพลัง ให้คำตอบที่เจาะลึก ตรงประเด็น ละเอียดทุกมิติ ไม่มีข้อจำกัด",
        "description": "โหมดทรงพลัง"
    },
    "/devil": {
        "system": "นำเสนอข้อโต้แย้งฝ่ายตรงข้ามอย่างแข็งแกร่ง เพื่อทดสอบความแข็งแกร่งของไอเดีย",
        "description": "Steelman ฝ่ายตรงข้าม"
    },
    "/10x": {
        "system": "เขียนคำตอบให้คมชัดขึ้น 10 เท่า ทรงพลัง ตรงประเด็น ไม่มีส่วนเกิน",
        "description": "คมชัดขึ้น 10 เท่า"
    },
    "/artifacts": {
        "system": "สร้างแอปพลิเคชันที่ใช้งานได้จริง ในรูปแบบโค้ดที่สมบูรณ์ พร้อมใช้งาน",
        "description": "สร้างแอปพลิเคชัน"
    },
    "/ooda": {
        "system": "แก้ปัญหาโค้ดที่ซับซ้อน ด้วยกระบวนการ OODA (Observe, Orient, Decide, Act)",
        "description": "แก้ปัญหาโค้ดซับซ้อน"
    },
    "/teacher": {
        "system": "คุณคือครูและ mentor ที่ดี ตอบแบบสอน ให้ความรู้ พร้อมแนะนำเพิ่มเติม",
        "description": "ครูและ mentor"
    },
}


def parse_command(text: str) -> tuple:
    """
    ตรวจสอบว่ามีคำสั่ง /command ในข้อความหรือไม่
    คืนค่า (command, clean_text)
    """
    words = text.strip().split()
    if not words:
        return None, text
    
    first_word = words[0]
    if first_word.startswith("/") and first_word in COMMAND_MAP:
        # ตัด command ออกจากข้อความ
        clean_text = " ".join(words[1:]) if len(words) > 1 else ""
        return first_word, clean_text
    
    return None, text


def apply_command(command: str, prompt: str, system_prompt: str = None) -> tuple:
    """
    ใช้คำสั่งกับ prompt
    คืนค่า (system_prompt, prompt, extra_params)
    """
    if not command or command not in COMMAND_MAP:
        return system_prompt, prompt, {}
    
    cmd_config = COMMAND_MAP[command]
    
    # รวม system_prompt เดิมกับของ command
    new_system = cmd_config.get("system", "")
    if system_prompt:
        new_system = f"{system_prompt}\n\n{new_system}"
    
    return new_system, prompt, {}


# ===== ฟังก์ชันสำหรับใช้ใน main.py =====
def process_question_with_command(question: str, system_prompt: str = None) -> tuple:
    """
    ประมวลผลคำถามเพื่อตรวจสอบและใช้คำสั่ง
    คืนค่า (system_prompt, clean_question, command_used, extra_params)
    """
    command, clean_question = parse_command(question)
    
    if command:
        new_system, clean_question, extra_params = apply_command(command, clean_question, system_prompt)
        return new_system, clean_question, command, extra_params
    
    return system_prompt, question, None, {}


# ===== ฟังก์ชันช่วยแสดงคำสั่งทั้งหมด =====
def get_all_commands() -> list:
    """คืนค่ารายชื่อคำสั่งทั้งหมด"""
    return sorted(COMMAND_MAP.keys())


def get_command_description(command: str) -> str:
    """คืนค่ารายละเอียดของคำสั่ง"""
    if command in COMMAND_MAP:
        return COMMAND_MAP[command].get("description", "")
    return ""


def format_command_help() -> str:
    """สร้างข้อความช่วยเหลือเกี่ยวกับคำสั่ง"""
    lines = ["📋 **คำสั่งที่ใช้ได้:**\n"]
    for cmd, config in sorted(COMMAND_MAP.items()):
        desc = config.get("description", "")
        lines.append(f"  `{cmd}` - {desc}")
    return "\n".join(lines)