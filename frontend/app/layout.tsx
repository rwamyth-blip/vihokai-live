// app/layout.tsx (ไฟล์หลัก - มี <html> และ <body> อันเดียว)
import "./globals.css"

export const metadata = {
  title: "VihokAI - AI ที่เข้าใจคุณ ทุกภาษา ทั่วโลก",
  description: "ถามอะไรก็ได้ — เขียนงาน คิดไอเดีย สรุปเอกสาร วางแผน",
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="th">
      <body className="bg-[#0f0f0f] text-white antialiased">
        {children}
      </body>
    </html>
  )
}