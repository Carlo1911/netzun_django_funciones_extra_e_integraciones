from django.urls import path
import apps.api.views as views

urlpatterns = [
    path("mailtrap", views.MailtrapEmail.as_view()),
    path("mailtrap-template", views.MailtrapTemplateEmail.as_view()),
    path("hotmail", views.HotmailProviderEmail.as_view()),
    path("gmail", views.GmailProviderEmail.as_view()),
    path("mailgun-anymail", views.MailgunAnymailProviderEmail.as_view()),
    path("mailgun-requests", views.MailgunRequestsProviderEmail.as_view()),
    path("qr-generator", views.QRGenerator.as_view()),
    path("excel-openpyxl", views.OpenpyxlExcel.as_view()),
    path("excel-xlsxwriter", views.XlsxwriterExcel.as_view()),
    path("pdf", views.PDFGenerator.as_view()),
]
