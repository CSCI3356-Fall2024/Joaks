# Generated by Django 5.1.2 on 2024-11-04 00:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_customuser_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='double_major',
            field=models.CharField(blank=True, choices=[('accounting', 'Accounting'), ('accounting_for_finance_and_consulting', 'Accounting for Finance and Consulting'), ('african_and_african_diaspora_studies', 'African and African Diaspora Studies'), ('american_heritage', 'American Heritage'), ('applied_data_science', 'Applied Data Science'), ('applied_liberal_arts', 'Applied Liberal Arts'), ('applied_physics', 'Applied Physics'), ('applied_psychology_and_human_development', 'Applied Psychology and Human Development'), ('art_history', 'Art History'), ('biochemistry', 'Biochemistry'), ('biology', 'Biology'), ('business', 'Business'), ('business_analytics', 'Business Analytics'), ('chemistry', 'Chemistry'), ('classics', 'Classics'), ('communication', 'Communication'), ('computer_science', 'Computer Science'), ('criminal_and_social_justice', 'Criminal and Social Justice'), ('cybersecurity', 'Cybersecurity'), ('digital_communications', 'Digital Communications'), ('economics', 'Economics'), ('elementary_education', 'Elementary Education'), ('english', 'English'), ('entrepreneurship', 'Entrepreneurship'), ('environmental_geoscience', 'Environmental Geoscience'), ('environmental_studies', 'Environmental Studies'), ('film_studies', 'Film Studies'), ('finance', 'Finance'), ('french', 'French'), ('general_business', 'General Business'), ('general_management', 'General Management'), ('geological_sciences', 'Geological Sciences'), ('german_studies', 'German Studies'), ('global_public_health_and_the_common_good', 'Global Public Health and the Common Good'), ('health_sciences', 'Health Sciences'), ('hispanic_studies', 'Hispanic Studies'), ('history', 'History'), ('human_centered_engineering', 'Human-Centered Engineering'), ('independent', 'Independent'), ('information_technology', 'Information Technology'), ('international_studies', 'International Studies'), ('islamic_civilization_and_societies', 'Islamic Civilization and Societies'), ('italian', 'Italian'), ('linguistics', 'Linguistics'), ('management_and_leadership', 'Management and Leadership'), ('marketing', 'Marketing'), ('mathematics', 'Mathematics'), ('mathematics_computer_science', 'Mathematics/Computer Science'), ('music', 'Music'), ('neuroscience', 'Neuroscience'), ('nursing', 'Nursing'), ('operations_management', 'Operations Management'), ('perspectives_on_spanish_america', 'Perspectives on Spanish America'), ('philosophy', 'Philosophy'), ('physics', 'Physics'), ('political_science', 'Political Science'), ('psychology', 'Psychology'), ('russian', 'Russian'), ('secondary_education', 'Secondary Education'), ('slavic_studies', 'Slavic Studies'), ('sociology', 'Sociology'), ('studio_art', 'Studio Art'), ('theatre', 'Theatre'), ('theology', 'Theology'), ('transformative_educational_studies', 'Transformative Educational Studies')], max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='double_minor',
            field=models.CharField(blank=True, choices=[('accounting', 'Accounting'), ('accounting_for_finance_and_consulting', 'Accounting for Finance and Consulting'), ('african_and_african_diaspora_studies', 'African and African Diaspora Studies'), ('american_heritage', 'American Heritage'), ('applied_data_science', 'Applied Data Science'), ('applied_liberal_arts', 'Applied Liberal Arts'), ('applied_physics', 'Applied Physics'), ('applied_psychology_and_human_development', 'Applied Psychology and Human Development'), ('art_history', 'Art History'), ('biochemistry', 'Biochemistry'), ('biology', 'Biology'), ('business', 'Business'), ('business_analytics', 'Business Analytics'), ('chemistry', 'Chemistry'), ('classics', 'Classics'), ('communication', 'Communication'), ('computer_science', 'Computer Science'), ('criminal_and_social_justice', 'Criminal and Social Justice'), ('cybersecurity', 'Cybersecurity'), ('digital_communications', 'Digital Communications'), ('economics', 'Economics'), ('elementary_education', 'Elementary Education'), ('english', 'English'), ('entrepreneurship', 'Entrepreneurship'), ('environmental_geoscience', 'Environmental Geoscience'), ('environmental_studies', 'Environmental Studies'), ('film_studies', 'Film Studies'), ('finance', 'Finance'), ('french', 'French'), ('general_business', 'General Business'), ('general_management', 'General Management'), ('geological_sciences', 'Geological Sciences'), ('german_studies', 'German Studies'), ('global_public_health_and_the_common_good', 'Global Public Health and the Common Good'), ('health_sciences', 'Health Sciences'), ('hispanic_studies', 'Hispanic Studies'), ('history', 'History'), ('human_centered_engineering', 'Human-Centered Engineering'), ('independent', 'Independent'), ('information_technology', 'Information Technology'), ('international_studies', 'International Studies'), ('islamic_civilization_and_societies', 'Islamic Civilization and Societies'), ('italian', 'Italian'), ('linguistics', 'Linguistics'), ('management_and_leadership', 'Management and Leadership'), ('marketing', 'Marketing'), ('mathematics', 'Mathematics'), ('mathematics_computer_science', 'Mathematics/Computer Science'), ('music', 'Music'), ('neuroscience', 'Neuroscience'), ('nursing', 'Nursing'), ('operations_management', 'Operations Management'), ('perspectives_on_spanish_america', 'Perspectives on Spanish America'), ('philosophy', 'Philosophy'), ('physics', 'Physics'), ('political_science', 'Political Science'), ('psychology', 'Psychology'), ('russian', 'Russian'), ('secondary_education', 'Secondary Education'), ('slavic_studies', 'Slavic Studies'), ('sociology', 'Sociology'), ('studio_art', 'Studio Art'), ('theatre', 'Theatre'), ('theology', 'Theology'), ('transformative_educational_studies', 'Transformative Educational Studies')], max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='major',
            field=models.CharField(blank=True, choices=[('accounting', 'Accounting'), ('accounting_for_finance_and_consulting', 'Accounting for Finance and Consulting'), ('african_and_african_diaspora_studies', 'African and African Diaspora Studies'), ('american_heritage', 'American Heritage'), ('applied_data_science', 'Applied Data Science'), ('applied_liberal_arts', 'Applied Liberal Arts'), ('applied_physics', 'Applied Physics'), ('applied_psychology_and_human_development', 'Applied Psychology and Human Development'), ('art_history', 'Art History'), ('biochemistry', 'Biochemistry'), ('biology', 'Biology'), ('business', 'Business'), ('business_analytics', 'Business Analytics'), ('chemistry', 'Chemistry'), ('classics', 'Classics'), ('communication', 'Communication'), ('computer_science', 'Computer Science'), ('criminal_and_social_justice', 'Criminal and Social Justice'), ('cybersecurity', 'Cybersecurity'), ('digital_communications', 'Digital Communications'), ('economics', 'Economics'), ('elementary_education', 'Elementary Education'), ('english', 'English'), ('entrepreneurship', 'Entrepreneurship'), ('environmental_geoscience', 'Environmental Geoscience'), ('environmental_studies', 'Environmental Studies'), ('film_studies', 'Film Studies'), ('finance', 'Finance'), ('french', 'French'), ('general_business', 'General Business'), ('general_management', 'General Management'), ('geological_sciences', 'Geological Sciences'), ('german_studies', 'German Studies'), ('global_public_health_and_the_common_good', 'Global Public Health and the Common Good'), ('health_sciences', 'Health Sciences'), ('hispanic_studies', 'Hispanic Studies'), ('history', 'History'), ('human_centered_engineering', 'Human-Centered Engineering'), ('independent', 'Independent'), ('information_technology', 'Information Technology'), ('international_studies', 'International Studies'), ('islamic_civilization_and_societies', 'Islamic Civilization and Societies'), ('italian', 'Italian'), ('linguistics', 'Linguistics'), ('management_and_leadership', 'Management and Leadership'), ('marketing', 'Marketing'), ('mathematics', 'Mathematics'), ('mathematics_computer_science', 'Mathematics/Computer Science'), ('music', 'Music'), ('neuroscience', 'Neuroscience'), ('nursing', 'Nursing'), ('operations_management', 'Operations Management'), ('perspectives_on_spanish_america', 'Perspectives on Spanish America'), ('philosophy', 'Philosophy'), ('physics', 'Physics'), ('political_science', 'Political Science'), ('psychology', 'Psychology'), ('russian', 'Russian'), ('secondary_education', 'Secondary Education'), ('slavic_studies', 'Slavic Studies'), ('sociology', 'Sociology'), ('studio_art', 'Studio Art'), ('theatre', 'Theatre'), ('theology', 'Theology'), ('transformative_educational_studies', 'Transformative Educational Studies')], max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='minor',
            field=models.CharField(blank=True, choices=[('accounting', 'Accounting'), ('accounting_for_finance_and_consulting', 'Accounting for Finance and Consulting'), ('african_and_african_diaspora_studies', 'African and African Diaspora Studies'), ('american_heritage', 'American Heritage'), ('applied_data_science', 'Applied Data Science'), ('applied_liberal_arts', 'Applied Liberal Arts'), ('applied_physics', 'Applied Physics'), ('applied_psychology_and_human_development', 'Applied Psychology and Human Development'), ('art_history', 'Art History'), ('biochemistry', 'Biochemistry'), ('biology', 'Biology'), ('business', 'Business'), ('business_analytics', 'Business Analytics'), ('chemistry', 'Chemistry'), ('classics', 'Classics'), ('communication', 'Communication'), ('computer_science', 'Computer Science'), ('criminal_and_social_justice', 'Criminal and Social Justice'), ('cybersecurity', 'Cybersecurity'), ('digital_communications', 'Digital Communications'), ('economics', 'Economics'), ('elementary_education', 'Elementary Education'), ('english', 'English'), ('entrepreneurship', 'Entrepreneurship'), ('environmental_geoscience', 'Environmental Geoscience'), ('environmental_studies', 'Environmental Studies'), ('film_studies', 'Film Studies'), ('finance', 'Finance'), ('french', 'French'), ('general_business', 'General Business'), ('general_management', 'General Management'), ('geological_sciences', 'Geological Sciences'), ('german_studies', 'German Studies'), ('global_public_health_and_the_common_good', 'Global Public Health and the Common Good'), ('health_sciences', 'Health Sciences'), ('hispanic_studies', 'Hispanic Studies'), ('history', 'History'), ('human_centered_engineering', 'Human-Centered Engineering'), ('independent', 'Independent'), ('information_technology', 'Information Technology'), ('international_studies', 'International Studies'), ('islamic_civilization_and_societies', 'Islamic Civilization and Societies'), ('italian', 'Italian'), ('linguistics', 'Linguistics'), ('management_and_leadership', 'Management and Leadership'), ('marketing', 'Marketing'), ('mathematics', 'Mathematics'), ('mathematics_computer_science', 'Mathematics/Computer Science'), ('music', 'Music'), ('neuroscience', 'Neuroscience'), ('nursing', 'Nursing'), ('operations_management', 'Operations Management'), ('perspectives_on_spanish_america', 'Perspectives on Spanish America'), ('philosophy', 'Philosophy'), ('physics', 'Physics'), ('political_science', 'Political Science'), ('psychology', 'Psychology'), ('russian', 'Russian'), ('secondary_education', 'Secondary Education'), ('slavic_studies', 'Slavic Studies'), ('sociology', 'Sociology'), ('studio_art', 'Studio Art'), ('theatre', 'Theatre'), ('theology', 'Theology'), ('transformative_educational_studies', 'Transformative Educational Studies')], max_length=50),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='role',
            field=models.CharField(choices=[('student', 'Student'), ('supervisor', 'Supervisor')], default='student', max_length=20),
        ),
    ]
