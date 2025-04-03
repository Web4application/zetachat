import { NotificationsProvider } from "./NotificationsProvider";
import { MyApp } from "./MyApp";

export default function Layout({ children }) {
  return (
    <NotificationsProvider>
      <MyApp />
    </NotificationsProvider>
  );
}
