import React from 'react';

interface ViHokLogoProps {
  className?: string;
}

export const ViHokLogo: React.FC<ViHokLogoProps> = ({ className = '' }) => {
  return (
    <div className={`flex items-center gap-2 ${className}`}>
      <svg
        width="32"
        height="32"
        viewBox="0 0 32 32"
        fill="none"
        xmlns="http://www.w3.org/2000/svg"
      >
        <circle cx="16" cy="16" r="16" fill="#4F46E5" />
        <path
          d="M10 10L22 22M10 22L22 10"
          stroke="white"
          strokeWidth="2.5"
          strokeLinecap="round"
        />
        <circle cx="16" cy="16" r="6" fill="white" />
      </svg>
      <span className="text-xl font-bold text-gray-800">ViHok AI</span>
    </div>
  );
};