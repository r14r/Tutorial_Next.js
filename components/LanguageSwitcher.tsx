"use client";
import { useRouter } from 'next/navigation';
import { usePathname } from 'next/navigation';

const languages = [
  { code: 'de', label: 'Deutsch' },
  { code: 'en', label: 'English' },
  { code: 'mr', label: 'मराठी' },
];

export default function LanguageSwitcher() {
  const router = useRouter();
  const pathname = usePathname();

  const handleChange = (e: React.ChangeEvent<HTMLSelectElement>) => {
    const lang = e.target.value;
    const segments = pathname.split('/');
    if (languages.some(l => l.code === segments[1])) {
      segments[1] = lang;
    } else {
      segments.splice(1, 0, lang);
    }
    router.push(segments.join('/'));
  };

  return (
    <select onChange={handleChange} defaultValue={languages[0].code}>
      {languages.map(lang => (
        <option key={lang.code} value={lang.code}>{lang.label}</option>
      ))}
    </select>
  );
}
