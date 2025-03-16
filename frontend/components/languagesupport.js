import i18n from "i18next";
import { initReactI18next } from "react-i18next";
import translationEN from "./locales/en.json";
import translationFR from "./locales/fr.json";

i18n.use(initReactI18next).init({
    resources: {
        en: { translation: translationEN },
        fr: { translation: translationFR },
    },
    lng: "en", // Default language
    fallbackLng: "en",
    interpolation: { escapeValue: false },
});

const Welcome = () => {
    const { t } = useTranslation();
    return <h1>{t('welcome_message')}</h1>;
};
