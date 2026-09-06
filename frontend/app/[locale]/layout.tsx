// app/[locale]/layout.tsx
// ✅ ไม่มี <html> + <body> - แค่ส่ง children ไป (เพราะ app/layout.tsx มีแล้ว)
import "../globals.css"

export const metadata = {
  title: "VihokAI - AI ที่เข้าใจคุณ ทุกภาษา ทั่วโลก",
  description: "ถามอะไรก็ได้ — เขียนงาน คิดไอเดีย สรุปเอกสาร วางแผน",
}

export default function RootLayout({
  children,
  params,
}: {
  children: React.ReactNode
  params: Promise<{ locale: string }>
}) {
  return (
    // ✅ แค่ children อย่างเดียว ไม่มี <html> และ <body>
    children
  )
}