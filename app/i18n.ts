import NextI18Next from 'next-i18next';
import i18nConfig from '../next-i18next.config.js';

const NextI18NextInstance = new NextI18Next(i18nConfig);

export default NextI18NextInstance;
export const { appWithTranslation, useTranslation } = NextI18NextInstance;
