

House Price Prediction

Smart Property Valuation and Comparison System

Project Type: Student Machine Learning Project
Prepared for: School Presentation / Student Competition
Repository: https://github.com/mjavadmzm-dev/house-price-prediction

بخش اول: نسخهٔ فارسی

۱. خلاصهٔ اجرایی

پروژهٔ House Price Prediction یک سامانهٔ نرم‌افزاری برای تخمین و مقایسهٔ قیمت خانه‌ها با استفاده از یادگیری ماشین است. هدف این پروژه، ارائهٔ یک ابزار ساده و قابل‌فهم برای کمک به کاربران در بررسی اولیهٔ ارزش احتمالی املاک است.

این سامانه با دریافت سه ویژگی اصلی هر خانه، شامل مساحت، تعداد اتاق‌ها و سن ساختمان، قیمت تخمینی آن را محاسبه می‌کند. کاربران همچنین می‌توانند سه خانه را هم‌زمان بررسی کرده و نتایج را در قالب یک جدول مقایسه کنند.

نسخهٔ فعلی پروژه با Python، کتابخانهٔ scikit-learn و رابط کاربری Streamlit ساخته شده است. در آینده می‌توان آن را با داده‌های معتبر بازار مسکن، امکانات بیشتر و یک مدل پیش‌بینی دقیق‌تر توسعه داد.

چشم‌انداز کسب‌وکار: تبدیل یک پروژهٔ آموزشی یادگیری ماشین به ابزاری کاربردی برای تحلیل اولیه و مقایسهٔ املاک.

۲. مسئله و نیاز بازار

انتخاب خانه برای خرید، فروش یا سرمایه‌گذاری به بررسی عوامل متعددی نیاز دارد. مقایسهٔ دستی چند ملک می‌تواند زمان‌بر باشد و کاربران ممکن است برای تخمین اولیهٔ قیمت به ابزارهای ساده و قابل‌دسترس نیاز داشته باشند.

مسائل اصلی که این پروژه قصد دارد به آن‌ها پاسخ دهد عبارت‌اند از:

دشواری مقایسهٔ سریع چند خانه.

نیاز به یک تخمین اولیه بر اساس مشخصات ملک.

پیچیدگی برخی ابزارهای تحلیل داده برای کاربران عادی.

نیاز دانش‌آموزان و علاقه‌مندان به یادگیری ماشین به نمونه‌ای عملی از کاربرد هوش مصنوعی.

این موارد، نیازهای احتمالی کاربران هستند و میزان تقاضای واقعی بازار هنوز باید با تحقیق و مصاحبه بررسی شود.

۳. راهکار پیشنهادی

این سامانه یک رابط کاربری ساده ارائه می‌دهد که کاربر می‌تواند اطلاعات خانه را وارد کند و قیمت پیش‌بینی‌شده را ببیند.

قابلیت‌های نسخهٔ فعلی:

دریافت مساحت خانه.

دریافت تعداد اتاق‌ها.

دریافت سن ساختمان.

پیش‌بینی قیمت با مدل رگرسیون خطی.

مقایسهٔ قیمت پیش‌بینی‌شدهٔ سه خانه.

نمایش نتایج در قالب جدول.

نمایش معیارهای ارزیابی مدل، شامل R² و میانگین قدر مطلق خطا (MAE).

قیمت خروجی، تخمین مدل است و نباید به‌عنوان قیمت قطعی معامله یا ارزیابی رسمی ملک استفاده شود.

۴. مشتریان هدف

مشتریان بالقوهٔ این محصول عبارت‌اند از:

خریداران خانه: برای مقایسهٔ اولیهٔ چند گزینه.

فروشندگان ملک: برای آشنایی مقدماتی با عوامل مؤثر بر تخمین قیمت.

مشاوران املاک: به‌عنوان ابزار کمکی برای بررسی اولیهٔ املاک.

دانش‌آموزان و دانشجویان: برای آشنایی عملی با یادگیری ماشین.

توسعه‌دهندگان نرم‌افزار: برای مطالعه و توسعهٔ یک پروژهٔ متن‌باز.

در مرحلهٔ نخست، کاربران آموزشی و علاقه‌مندان به فناوری مناسب‌ترین گروه برای آزمایش محصول هستند. ورود به بازار حرفه‌ای املاک به اعتبارسنجی بیشتر نیاز دارد.

۵. ارزش پیشنهادی و مزیت رقابتی

ارزش پیشنهادی این پروژه، ساده‌کردن فرایند تخمین اولیه و مقایسهٔ چند خانه است.

مزیت‌های بالقوه:

رابط کاربری ساده و قابل‌فهم.

مقایسهٔ هم‌زمان سه خانه.

استفاده از یک مدل یادگیری ماشین واقعی در نرم‌افزار.

نمایش معیارهای عملکرد مدل.

ساختار قابل توسعه و امکان مشارکت در پروژه از طریق GitHub.

هزینهٔ اولیهٔ پایین برای ساخت نمونهٔ آموزشی.

این مزیت‌ها به معنی برتری اثبات‌شده نسبت به وب‌سایت‌های حرفه‌ای املاک نیستند. چنین ادعایی به آزمایش و مقایسه با محصولات موجود نیاز دارد.

۶. مدل فنی و وضعیت فعلی محصول

فناوری‌های مورد استفاده:

فناوری

کاربرد

Python

زبان اصلی برنامه‌نویسی

pandas

آماده‌سازی و مدیریت داده‌ها

scikit-learn

آموزش مدل رگرسیون خطی

joblib

ذخیره و بارگذاری مدل آموزش‌دیده

Streamlit

ساخت رابط کاربری

Git و GitHub

مدیریت نسخه و انتشار کد

مدل فعلی از سه ویژگی مساحت، تعداد اتاق‌ها و سن ساختمان استفاده می‌کند.

داده‌های آزمایشی فعلی برای نمایش عملکرد نرم‌افزار مناسب‌اند، اما تا زمانی که منبع و کیفیت داده‌های واقعی بازار بررسی نشده باشد، نمی‌توان عملکرد مدل را در معاملات واقعی تأیید کرد.

معیارهای R² و MAE که برنامه نمایش می‌دهد، باید در کنار نوع داده، روش تقسیم داده‌ها و نتایج آزمون تفسیر شوند. خطای MAE نیز در همان واحدی است که قیمت‌های مجموعهٔ داده با آن ثبت شده‌اند.

۷. تحلیل رقبا

رقبای احتمالی این محصول در چهار گروه قرار می‌گیرند:

وب‌سایت‌های آگهی و جست‌وجوی املاک.

ابزارهای آنلاین تخمین قیمت خانه.

نرم‌افزارهای تخصصی تحلیل بازار مسکن.

روش‌های دستی مقایسهٔ قیمت توسط کاربران یا مشاوران.

در وضعیت فعلی، مزیت اصلی پروژه آموزشی‌بودن، سادگی و قابلیت توسعه است؛ نه دسترسی به داده‌های گسترده یا دقت اثبات‌شدهٔ بالاتر از رقبا.

برای تکمیل تحلیل رقابتی، باید چند محصول واقعی بررسی شوند و امکانات، هزینه‌ها، بازار هدف و محدودیت‌های آن‌ها با این پروژه مقایسه شود.

۸. مدل درآمدی پیشنهادی

درآمدزایی هنوز بخشی از قابلیت‌های اجراشدهٔ پروژه نیست. مدل‌های زیر فقط فرضیه‌هایی برای آینده هستند:

مدل اول: نسخهٔ رایگان و نسخهٔ حرفه‌ای

نسخهٔ پایه برای استفادهٔ عمومی رایگان باشد و در صورت اثبات نیاز بازار، امکانات پیشرفته به نسخهٔ پولی اضافه شوند.

مدل دوم: اشتراک برای مشاوران املاک

در آینده می‌توان ابزارهای مقایسه، گزارش‌گیری و مدیریت مجموعه‌ای از املاک را برای کاربران حرفه‌ای ارائه کرد.

مدل سوم: خدمات سفارشی

پس از کسب تجربه، امکان توسعه یا شخصی‌سازی ابزارهای تحلیل املاک برای مشتریان سازمانی بررسی شود.

مدل چهارم: محصول آموزشی

پروژه می‌تواند به‌عنوان نمونهٔ آموزشی یا ابزار نمایش مفاهیم یادگیری ماشین استفاده شود.

هیچ‌یک از این مدل‌ها در حال حاضر درآمد تأییدشده‌ای ایجاد نکرده است. انتخاب مدل نهایی باید بر اساس بازخورد کاربران و هزینه‌های واقعی انجام شود.

۹. برنامهٔ بازاریابی و جذب کاربران

برنامهٔ اولیهٔ بازاریابی شامل این مراحل است:

انتشار کد و مستندات در GitHub.

تهیهٔ یک ویدئوی کوتاه از اجرای برنامه و مقایسهٔ سه خانه.

افزودن تصاویر رابط کاربری به README.

ارائهٔ پروژه در مدرسه یا مسابقات دانش‌آموزی.

دریافت بازخورد از هم‌کلاسی‌ها، معلمان و کاربران آزمایشی.

اصلاح رابط کاربری و افزودن قابلیت‌ها بر اساس بازخوردها.

در مراحل بعد، می‌توان نسخهٔ آنلاین آزمایشی ایجاد کرد تا کاربران بدون نصب Python برنامه را بررسی کنند.

۱۰. برنامهٔ عملیاتی و توسعه

مرحلهٔ اول: تکمیل نمونهٔ اولیه

بررسی عملکرد تمام قابلیت‌های موجود.

بهبود مستندات نصب و اجرا.

بررسی مدیریت خطاهای ورودی.

مشخص‌کردن محدودیت‌های مدل و داده‌ها.

مرحلهٔ دوم: اعتبارسنجی

تهیهٔ داده‌های واقعی و مجاز بازار مسکن.

ثبت منبع، تاریخ و واحد قیمت‌ها.

بررسی کیفیت و کامل‌بودن داده‌ها.

مقایسهٔ عملکرد مدل با یک روش پایهٔ ساده.

آزمایش مدل روی داده‌هایی که در آموزش استفاده نشده‌اند.

مرحلهٔ سوم: توسعهٔ محصول

اضافه‌کردن نمودارهای مقایسه‌ای.

امکان ذخیره یا دریافت گزارش نتایج.

بررسی اثر ویژگی‌های مختلف بر پیش‌بینی.

بهبود اعتبارسنجی ورودی‌ها.

بررسی امکان میزبانی آنلاین.

مرحلهٔ چهارم: بررسی تجاری‌سازی

مصاحبه با کاربران بالقوه.

بررسی محصولات رقیب.

تخمین هزینه‌های نگهداری و توسعه.

آزمایش تمایل کاربران به پرداخت.

تصمیم‌گیری دربارهٔ ادامهٔ توسعهٔ تجاری.

۱۱. برنامهٔ مالی و فرضیات اقتصادی

از آنجا که پروژه در مرحلهٔ نمونهٔ اولیه قرار دارد، هنوز اطلاعات کافی برای ارائهٔ درآمد، سود یا هزینهٔ قطعی وجود ندارد.

هزینه‌های احتمالی

مورد

وضعیت

توسعهٔ اولیه

عمدتاً با استفاده از زمان برنامه‌نویسی و ابزارهای موجود

رایانه و اینترنت

هزینهٔ واقعی شخصی هنوز محاسبه نشده است

میزبانی آنلاین

به انتخاب سرویس و میزان مصرف بستگی دارد

تهیه و پاک‌سازی داده

به منبع و مجوز استفاده از داده بستگی دارد

نگهداری و پشتیبانی

با افزایش کاربران ممکن است بیشتر شود

بازاریابی

در مرحلهٔ فعلی بودجهٔ تأییدشده‌ای ندارد

سناریوهای مالی آینده

سناریوی کم‌هزینه: پروژه به‌صورت متن‌باز و آموزشی باقی بماند و فقط در صورت نیاز برای میزبانی یا تهیهٔ داده هزینه شود.

سناریوی آزمایشی تجاری: نسخه‌ای محدود برای گروه کوچکی از کاربران ارائه شود و هزینه‌ها و بازخوردها اندازه‌گیری شوند.

سناریوی توسعه‌یافته: پس از تأیید نیاز بازار، امکانات حرفه‌ای و مدل درآمدی مشخصی طراحی شوند.

برای محاسبهٔ نقطهٔ سربه‌سر در آینده می‌توان از فرمول زیر استفاده کرد:

نقطهٔ سربه‌سر تعداد مشتریان = هزینهٔ ثابت ماهانه ÷ (درآمد هر مشتری − هزینهٔ متغیر هر مشتری)

این فرمول زمانی قابل استفاده است که هزینه‌ها و قیمت فروش واقعی مشخص شده باشند. در حال حاضر، هیچ درآمد یا سود فرضی نباید به‌عنوان نتیجهٔ واقعی پروژه معرفی شود.

۱۲. ریسک‌ها و راهکارهای کاهش آن‌ها

ریسک اول: داده‌های غیرواقعی یا محدود

اگر داده‌ها نمایندهٔ بازار واقعی نباشند، پیش‌بینی‌ها ممکن است در عمل قابل اعتماد نباشند.

راهکار: استفاده از داده‌های معتبر و مجاز، بررسی کیفیت داده‌ها و آزمایش مستقل مدل.

ریسک دوم: نادیده‌گرفتن عوامل مؤثر بر قیمت

قیمت خانه علاوه بر مساحت، تعداد اتاق‌ها و سن ساختمان به عواملی مانند موقعیت مکانی، امکانات، وضعیت بنا و شرایط بازار نیز وابسته است.

راهکار: افزودن تدریجی ویژگی‌های مفید در صورت دسترسی به داده‌های معتبر.

ریسک سوم: تغییر شرایط بازار

رابطهٔ بین ویژگی‌های خانه و قیمت ممکن است در زمان‌ها یا مناطق مختلف تغییر کند.

راهکار: پایش کیفیت مدل و آموزش مجدد در صورت وجود داده‌های به‌روز و کافی.

ریسک چهارم: اعتماد بیش از حد به خروجی مدل

کاربر ممکن است قیمت تخمینی را قیمت قطعی تلقی کند.

راهکار: نمایش هشدار واضح دربارهٔ ماهیت تخمینی نتیجه و محدودیت‌های مدل.

ریسک پنجم: هزینهٔ جذب مشتری و نبود تقاضای کافی

ممکن است کاربران حاضر به پرداخت هزینه برای این ابزار نباشند.

راهکار: مصاحبه با کاربران، آزمایش نمونهٔ اولیه و بررسی تمایل به پرداخت قبل از سرمایه‌گذاری جدی.

۱۳. ملاحظات اخلاقی و مسئولیت‌پذیری

نتایج باید به‌عنوان تخمین نمایش داده شوند، نه قیمت قطعی یا کارشناسی رسمی.

منبع و محدودیت‌های داده‌ها باید شفاف باشند.

داده‌های شخصی یا اطلاعات حساس املاک نباید بدون مجوز مناسب جمع‌آوری یا منتشر شوند.

عملکرد مدل باید برای مناطق و انواع مختلف املاک بررسی شود.

تصمیم‌های مهم مالی نباید صرفاً بر اساس خروجی این مدل گرفته شوند.

۱۴. شاخص‌های سنجش موفقیت

برای ارزیابی پیشرفت پروژه می‌توان شاخص‌های زیر را اندازه‌گیری کرد:

تعداد کاربران آزمایشی.

درصد کاربرانی که موفق به انجام پیش‌بینی می‌شوند.

میزان رضایت کاربران از سادگی رابط کاربری.

مقدار MAE روی یک مجموعهٔ آزمون معتبر و مستقل.

میزان بهبود عملکرد نسبت به روش پایه.

تعداد خطاهای نرم‌افزاری گزارش‌شده.

تعداد بازخوردهای قابل‌استفاده برای بهبود محصول.

برای این شاخص‌ها هنوز هدف‌های عددی تأییدشده تعیین نشده‌اند. پس از جمع‌آوری داده‌های اولیه می‌توان اهداف واقع‌بینانه مشخص کرد.

۱۵. جمع‌بندی

House Price Prediction یک پروژهٔ آموزشی کاربردی است که نشان می‌دهد چگونه می‌توان از Python و یادگیری ماشین برای ساخت یک ابزار تخمین و مقایسهٔ قیمت خانه استفاده کرد.

قابلیت مقایسهٔ سه خانه، رابط کاربری Streamlit و نمایش معیارهای ارزیابی، پایه‌ای مناسب برای توسعهٔ بیشتر فراهم می‌کنند. با این حال، ورود به بازار واقعی به داده‌های معتبر، ارزیابی مستقل مدل، بررسی نیاز مشتریان و برنامه‌ریزی مالی نیاز دارد.

هدف نهایی این طرح، توسعهٔ تدریجی پروژه بر اساس شواهد و بازخورد کاربران است؛ نه ادعای موفقیت تجاری پیش از آزمایش بازار.

Part Two: English Version

1. Executive Summary

House Price Prediction is a software project that estimates and compares house prices using machine learning. Its purpose is to provide a simple, accessible tool for preliminary property price estimation.

The current application uses three property features: area, number of rooms, and building age. It predicts a price for each property and allows users to compare three houses in a table.

The project is built with Python, scikit-learn, joblib, and Streamlit. Future development may include reliable real-estate data, additional property features, improved model evaluation, and online access.

Business vision: To develop an educational machine learning prototype into a useful tool for preliminary property analysis and comparison.

2. Problem and Market Need

Buying or selling a property involves comparing multiple factors. Manually comparing several properties can take time, and users may benefit from a simple tool that provides an initial estimate based on property characteristics.

Potential problems addressed by the project include:

Difficulty comparing several properties quickly.

The need for preliminary price estimates.

The complexity of some data-analysis tools.

The need for practical examples of machine learning in education.

These are potential user needs, not proven market demand. Further research and user interviews are required to validate them.

3. Proposed Solution

The application provides a simple interface where users enter property information and receive a predicted price.

Current features include:

Entering property area.

Entering the number of rooms.

Entering building age.

Predicting prices using linear regression.

Comparing three houses at the same time.

Displaying results in a table.

Showing model evaluation metrics, including R² and Mean Absolute Error (MAE).

The predicted price is an estimate. It is not a guaranteed sale price or a professional property valuation.

4. Target Customers

Potential customer groups include:

Home buyers: For preliminary comparisons between properties.

Home sellers: For an initial understanding of factors affecting estimated prices.

Real-estate agents: As a supporting tool for preliminary analysis.

Students and educators: For learning practical machine learning.

Software developers: For studying and extending an open-source project.

During the initial stage, students and technology enthusiasts are the most practical users for testing the product. Serving professional real-estate customers would require additional validation.

5. Value Proposition and Competitive Advantage

The proposed value is to simplify preliminary price estimation and property comparison.

Potential advantages include:

A simple user interface.

Simultaneous comparison of three properties.

Integration of a machine learning model into a working application.

Display of model evaluation metrics.

An extensible project published on GitHub.

Low initial development requirements for an educational prototype.

These are potential advantages, not proven superiority over established property platforms. A proper competitive evaluation is still needed.

6. Technology and Current Product Status

Technology

Purpose

Python

Main programming language

pandas

Data preparation and management

scikit-learn

Linear regression model

joblib

Saving and loading the trained model

Streamlit

User interface

Git and GitHub

Version control and code publication

The current model uses area, number of rooms, and building age.

The existing experimental dataset is suitable for demonstrating the application, but its results cannot establish real-market accuracy without reliable, representative property data and independent testing.

R² and MAE should be interpreted alongside the dataset, evaluation procedure, and test results. MAE is expressed in the same price unit as the dataset.

7. Competitive Analysis

Potential alternatives fall into four groups:

Property listing websites.

Online house-price estimation tools.

Professional real-estate analytics software.

Manual property comparisons performed by buyers or agents.

The project's current strengths are its educational value, simplicity, and extensibility—not proven higher accuracy or access to a larger market dataset.

A future competitive study should compare selected real products, their features, pricing, target users, and limitations.

8. Proposed Revenue Model

Revenue generation is not currently an implemented feature. The following are hypotheses for future evaluation.

Model A: Free and premium versions

Offer a free basic tool and consider paid advanced features if users demonstrate a clear need.

Model B: Subscription for real-estate professionals

Potential future features could include advanced comparisons, reporting, and property management.

Model C: Custom development services

After gaining experience, customized property-analysis tools could be explored for organizations.

Model D: Educational product

The application could serve as a learning resource or demonstration of machine learning concepts.

None of these models currently represents verified project revenue. The final choice should depend on user feedback and actual operating costs.

9. Marketing and User Acquisition

The initial marketing plan includes:

Publishing the code and documentation on GitHub.

Creating a short demonstration video.

Adding screenshots to the README.

Presenting the project at school or student competitions.

Collecting feedback from classmates, teachers, and test users.

Improving the application based on that feedback.

A hosted demonstration may be considered later so users can test the application without installing Python.

10. Operational and Development Roadmap

Phase 1: Complete the Prototype

Test all current features.

Improve installation and usage documentation.

Review input validation and error handling.

Document the model's limitations.

Phase 2: Validate the Model

Obtain reliable and legally usable real-estate data.

Record data sources, dates, and price units.

Check data quality and completeness.

Compare the model with a simple baseline.

Evaluate performance on data not used during training.

Phase 3: Improve the Product

Add visual comparison charts.

Consider downloadable reports.

Investigate how different features affect predictions.

Improve input validation.

Evaluate online hosting options.

Phase 4: Assess Commercial Potential

Interview potential users.

Research competing products.

Estimate maintenance and development costs.

Test willingness to pay.

Decide whether commercial development is justified.

11. Financial Plan and Economic Assumptions

The project is currently a prototype. There is not enough verified information to state actual revenue, profit, or total operating costs.

Potential Costs

Item

Current understanding

Initial development

Mainly developer time and existing tools

Computer and internet

Actual personal costs have not been calculated

Online hosting

Depends on the selected service and usage

Data acquisition and cleaning

Depends on data sources and usage permissions

Maintenance and support

May increase as usage grows

Marketing

No verified marketing budget is available

Future Financial Scenarios

Low-cost scenario: Keep the project open-source and educational, with expenses only when hosting or data acquisition is needed.

Pilot business scenario: Offer a limited version to a small group of users and measure costs and feedback.

Expanded business scenario: Develop professional features and a defined revenue model after validating market demand.

A future break-even calculation can use the following formula:

Break-even number of customers = Fixed monthly costs ÷ (Revenue per customer − Variable cost per customer)

This formula can be applied once actual prices and costs are known. Hypothetical revenue or profit must not be presented as actual project results.

12. Risks and Mitigation

Risk 1: Limited or unrealistic data

A dataset that does not represent the real market may produce unreliable real-world predictions.

Mitigation: Use reliable, legally usable data and conduct independent model evaluation.

Risk 2: Missing price-related features

Property prices depend on more than area, room count, and age. Location, amenities, condition, and market conditions may also matter.

Mitigation: Add useful features when reliable data becomes available.

Risk 3: Changing market conditions

The relationship between property characteristics and prices may change across locations and over time.

Mitigation: Monitor model performance and retrain when sufficient updated data is available.

Risk 4: Overreliance on predictions

Users may interpret estimates as guaranteed prices.

Mitigation: Clearly communicate that predictions are estimates and explain the model's limitations.

Risk 5: Insufficient demand

Potential customers may not be willing to pay for the product.

Mitigation: Interview users, test the prototype, and assess willingness to pay before making major investments.

13. Ethics and Responsible Use

Present outputs as estimates, not guaranteed prices or official valuations.

Disclose data sources and limitations.

Do not collect or publish sensitive property or personal information without appropriate authorization.

Evaluate performance across different property types and locations.

Do not encourage major financial decisions based solely on this model.

14. Success Metrics

Potential measures of progress include:

Number of test users.

Percentage of users who successfully complete a prediction.

User satisfaction with the interface.

MAE on a valid, independent test dataset.

Improvement over a baseline model.

Number of reported software issues.

Number of useful user feedback items.

No numerical targets have been validated yet. Realistic targets can be established after collecting initial results.

15. Conclusion

House Price Prediction is a practical educational project demonstrating how Python and machine learning can support preliminary property price estimation and comparison.

The three-property comparison feature, Streamlit interface, and model evaluation metrics provide a foundation for further development. However, commercial deployment would require reliable data, independent model validation, customer research, and a realistic financial plan.

The objective is to grow the project through evidence, testing, and user feedback—not to claim commercial success before the market has been validated.