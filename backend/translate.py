"""
ระบบแปลภาษา ใช้ AI (Groq / OpenAI / Gemini)
รองรับการแปลหลายภาษา
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import asyncio
import os

router = APIRouter(prefix="/api", tags=["translate"])


class TranslateRequest(BaseModel):
	text: str
	source: str = "auto"  # auto = ตรวจจับอัตโนมัติ
	target: str


class TranslateResponse(BaseModel):
	source: str
	target: str
	original: str
	translation: str


SUPPORTED_LANGUAGES = [
	{"code": "th", "name": "Thai", "native": "ไทย"},
	{"code": "en", "name": "English", "native": "English"},
	{"code": "zh", "name": "Chinese", "native": "中文"},
	{"code": "ja", "name": "Japanese", "native": "日本語"},
	{"code": "ko", "name": "Korean", "native": "한국어"},
	{"code": "vi", "name": "Vietnamese", "native": "Tiếng Việt"},
	{"code": "id", "name": "Indonesian", "native": "Bahasa Indonesia"},
	{"code": "ms", "name": "Malay", "native": "Bahasa Melayu"},
	{"code": "hi", "name": "Hindi", "native": "हिन्दी"},
	{"code": "bn", "name": "Bengali", "native": "বাংলা"},
	{"code": "ur", "name": "Urdu", "native": "اردو"},
	{"code": "ta", "name": "Tamil", "native": "தமிழ்"},
	{"code": "te", "name": "Telugu", "native": "తెలుగు"},
	{"code": "mr", "name": "Marathi", "native": "मराठी"},
	{"code": "gu", "name": "Gujarati", "native": "ગુજરાતી"},
	{"code": "kn", "name": "Kannada", "native": "ಕನ್ನಡ"},
	{"code": "ml", "name": "Malayalam", "native": "മലയാളം"},
	{"code": "pa", "name": "Punjabi", "native": "ਪੰਜਾਬੀ"},
	{"code": "ne", "name": "Nepali", "native": "नेपाली"},
	{"code": "si", "name": "Sinhala", "native": "සිංහල"},
	{"code": "my", "name": "Burmese", "native": "မြန်မာ"},
	{"code": "km", "name": "Khmer", "native": "ភាសាខ្មែរ"},
	{"code": "lo", "name": "Lao", "native": "ລາວ"},
	{"code": "fil", "name": "Filipino", "native": "Filipino"},
	{"code": "tl", "name": "Tagalog", "native": "Tagalog"},
	{"code": "jv", "name": "Javanese", "native": "Basa Jawa"},
	{"code": "su", "name": "Sundanese", "native": "Basa Sunda"},
	{"code": "ceb", "name": "Cebuano", "native": "Cebuano"},
	{"code": "mn", "name": "Mongolian", "native": "Монгол"},
	{"code": "kk", "name": "Kazakh", "native": "Қазақша"},
	{"code": "uz", "name": "Uzbek", "native": "O'zbekcha"},
	{"code": "tg", "name": "Tajik", "native": "Тоҷикӣ"},
	{"code": "ky", "name": "Kyrgyz", "native": "Кыргызча"},
	{"code": "tk", "name": "Turkmen", "native": "Türkmençe"},
	{"code": "es", "name": "Spanish", "native": "Español"},
	{"code": "fr", "name": "French", "native": "Français"},
	{"code": "de", "name": "German", "native": "Deutsch"},
	{"code": "it", "name": "Italian", "native": "Italiano"},
	{"code": "pt", "name": "Portuguese", "native": "Português"},
	{"code": "ru", "name": "Russian", "native": "Русский"},
	{"code": "uk", "name": "Ukrainian", "native": "Українська"},
	{"code": "pl", "name": "Polish", "native": "Polski"},
	{"code": "nl", "name": "Dutch", "native": "Nederlands"},
	{"code": "sv", "name": "Swedish", "native": "Svenska"},
	{"code": "da", "name": "Danish", "native": "Dansk"},
	{"code": "no", "name": "Norwegian", "native": "Norsk"},
	{"code": "fi", "name": "Finnish", "native": "Suomi"},
	{"code": "is", "name": "Icelandic", "native": "Íslenska"},
	{"code": "et", "name": "Estonian", "native": "Eesti"},
	{"code": "lv", "name": "Latvian", "native": "Latviešu"},
	{"code": "lt", "name": "Lithuanian", "native": "Lietuvių"},
	{"code": "cs", "name": "Czech", "native": "Čeština"},
	{"code": "sk", "name": "Slovak", "native": "Slovenčina"},
	{"code": "sl", "name": "Slovenian", "native": "Slovenščina"},
	{"code": "hr", "name": "Croatian", "native": "Hrvatski"},
	{"code": "sr", "name": "Serbian", "native": "Српски"},
	{"code": "bs", "name": "Bosnian", "native": "Bosanski"},
	{"code": "bg", "name": "Bulgarian", "native": "Български"},
	{"code": "ro", "name": "Romanian", "native": "Română"},
	{"code": "hu", "name": "Hungarian", "native": "Magyar"},
	{"code": "el", "name": "Greek", "native": "Ελληνικά"},
	{"code": "sq", "name": "Albanian", "native": "Shqip"},
	{"code": "mk", "name": "Macedonian", "native": "Македонски"},
	{"code": "ca", "name": "Catalan", "native": "Català"},
	{"code": "eu", "name": "Basque", "native": "Euskara"},
	{"code": "gl", "name": "Galician", "native": "Galego"},
	{"code": "ar", "name": "Arabic", "native": "العربية"},
	{"code": "he", "name": "Hebrew", "native": "עברית"},
	{"code": "fa", "name": "Persian", "native": "فارسی"},
	{"code": "tr", "name": "Turkish", "native": "Türkçe"},
	{"code": "az", "name": "Azerbaijani", "native": "Azərbaycanca"},
	{"code": "ka", "name": "Georgian", "native": "ქართული"},
	{"code": "hy", "name": "Armenian", "native": "Հայերեն"},
	{"code": "ku", "name": "Kurdish", "native": "Kurdî"},
	{"code": "ps", "name": "Pashto", "native": "پښتو"},
	{"code": "sw", "name": "Swahili", "native": "Kiswahili"},
	{"code": "am", "name": "Amharic", "native": "አማርኛ"},
	{"code": "ha", "name": "Hausa", "native": "Hausa"},
	{"code": "yo", "name": "Yoruba", "native": "Yorùbá"},
	{"code": "ig", "name": "Igbo", "native": "Igbo"},
	{"code": "zu", "name": "Zulu", "native": "isiZulu"},
	{"code": "xh", "name": "Xhosa", "native": "isiXhosa"},
	{"code": "rw", "name": "Kinyarwanda", "native": "Kinyarwanda"},
	{"code": "so", "name": "Somali", "native": "Soomaali"},
	{"code": "sn", "name": "Shona", "native": "chiShona"},
	{"code": "af", "name": "Afrikaans", "native": "Afrikaans"},
	{"code": "mg", "name": "Malagasy", "native": "Malagasy"},
	{"code": "ny", "name": "Chichewa", "native": "Chichewa"},
	{"code": "st", "name": "Sesotho", "native": "Sesotho"},
	{"code": "tn", "name": "Setswana", "native": "Setswana"},
	{"code": "ts", "name": "Tsonga", "native": "itsonga"},
	{"code": "la", "name": "Latin", "native": "Latina"},
	{"code": "eo", "name": "Esperanto", "native": "Esperanto"},
	{"code": "swb", "name": "Comorian", "native": "Shikomori"},
	{"code": "mi", "name": "Maori", "native": "Māori"},
	{"code": "sm", "name": "Samoan", "native": "Gagana Samoa"},
	{"code": "to", "name": "Tongan", "native": "Lea faka-Tonga"},
	{"code": "fj", "name": "Fijian", "native": "Na Vosa Vakaviti"},
	{"code": "ty", "name": "Tahitian", "native": "Reo Tahiti"},
	{"code": "haw", "name": "Hawaiian", "native": "ʻŌlelo Hawaiʻi"},
	{"code": "de-CH", "name": "Swiss German", "native": "Schwiizerdütsch"},
	{"code": "yue", "name": "Cantonese", "native": "粵語"},
	{"code": "ckb", "name": "Central Kurdish", "native": "کوردی"},
]


async def translate_with_ai(text: str, source: str, target: str) -> str:
	"""
	แปลข้อความโดยใช้ AI (Groq, OpenAI, Gemini)
	"""
	if not text.strip():
		return ""

	providers = (
		("call_groq", f"""
		แปลข้อความต่อไปนี้จากภาษา {source} เป็นภาษา {target}
		(แปลให้ถูกต้อง ตรงความหมาย และเป็นธรรมชาติ)

		ข้อความ: {text}

		คำแปล:
		""", "th"),
		("call_openai", f"""
		Translate the following text from {source} to {target}.
		Provide only the translation, nothing else.

		Text: {text}

		Translation:
		""", "en"),
		("call_gemini", f"""
		แปลข้อความต่อไปนี้จากภาษา {source} เป็นภาษา {target}
		ให้แปลอย่างถูกต้องและเป็นธรรมชาติ ตอบเฉพาะคำแปลเท่านั้น

		ข้อความ: {text}
		""", "th"),
	)
	for name, prompt, locale in providers:
		try:
			from main import __dict__ as main_namespace
			provider = main_namespace.get(name)
			if provider is None:
				continue
			result = await provider(prompt, locale)
			if result and not result.startswith(("Error", "❌")):
				return result.strip()
		except Exception as exc:
			print(f"⚠️ {name} translation failed: {exc}")
	return f"[ไม่สามารถแปลได้] {text}"


@router.get("/languages", response_model=list)
async def get_languages():
	return SUPPORTED_LANGUAGES


@router.post("/translate", response_model=TranslateResponse)
async def translate_text(req: TranslateRequest):
	"""แปลข้อความ"""
	text = req.text.strip()
	target = req.target.strip()
	source = req.source.strip() or "auto"
	if not text:
		raise HTTPException(status_code=400, detail="ข้อความไม่สามารถเว้นว่างได้")

	target_codes = [lang["code"] for lang in SUPPORTED_LANGUAGES]
	if target not in target_codes:
		raise HTTPException(status_code=400, detail=f"ไม่รองรับภาษาปลายทาง: {target}")
	if source != "auto" and source not in target_codes:
		raise HTTPException(status_code=400, detail=f"ไม่รองรับภาษาต้นทาง: {source}")

	translation = await translate_with_ai(text, source, target)
	return TranslateResponse(
		source=source,
		target=target,
		original=text,
		translation=translation,
	)


async def translate_text_async(text: str, target_lang: str = "th", source_lang: str = "auto") -> str:
	return await translate_with_ai(text, source_lang, target_lang)
