import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

# Скопируйте DSN из вашего личного кабинета на Sentry: 
# Settings → Projects → <ваш-проект> → Client Keys (DSN).
sentry_sdk.init(
    # В этой переменной будет значение для вашего проекта.
    dsn="https://e83311209ac74037aa35cabe9273c813@o4505592204558336.ingest.sentry.io/4505592208883712",
    integrations=[
        DjangoIntegration(),
    ],
    traces_sample_rate=1.0,
    send_default_pii=True
) 
