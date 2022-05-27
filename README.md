### Технические требования:
* Использование сверточной нейронной сети YOLO для детектирования объектов
* Использование библиотеки ffmpeg для предварительной обработки видеозаписи
* Использование CVAT/Roboflow в качестве инструмента разметки данных
* Использование алгоритма DeepSort для отслеживания объектов
* Использование контейнеров Docker для развертывания на сервер
* Использование базы данных PostgreSQL для сбора статистики
* Использование фреймворка GStreamer для работы с потоковыми данными

***

### Установка DeepSort (в консоли):
1. Создание и активация вирутального окружения
- Для Windows:
```
python -m venv venv
venv\Scripts\activate
```
- Для Linux/MacOS:
```
python -m venv venv
source venv/bin/activate
```
2. Переход в папку с Deepsort
```
cd Yolov5_DeepSort_OSNet
```
3. Установка зависимости из репозитория
```
pip install -qr requirements.txt
```
4. Переход в корень каталога и копирование папки weights в Yolov5_DeepSort_Pytorch
```
cd ..
cp -R weights Yolov5_DeepSort_OSNet/yolov5
```
5. Запуск test.py для проверки установки
6. Переход в папку Yolov5_DeepSort_OSNet для запуска
```
cd Yolov5_DeepSort_OSNet
```
7. Строка для трекинга 
```
python track.py --source .\video\video.mp4 --project .\ --save-txt --save-vid --yolo_model .\weights\best.pt --exist-ok
```

***

Запуск программы:
В папку video переносим нужное нам видео с названием "video.mp4"
Активируем виртуальное окружение (Если активировано - пропускаем)
Пишем: cd Yolov5_DeepSort_OSNet
Затем: python track.py --source .\video\video.mp4 --project .\ --save-txt --save-vid --yolo_model .\weights\best.pt --exist-ok
Вместо "." пишем путь к папке, где находится нейронка. Пример: E:\Neironka\

***

Создание таблицы Postgresql:
CREATE TABLE "public.detect" (
  "frame_idx" bigint NOT NULL,
  "id" bigint NOT NULL,
  "bbox_left" bigint NOT NULL,
  "bbox_top" bigint NOT NULL,
  "bbox_w" bigint NOT NULL,
  "bbox_h" bigint NOT NULL
)

### 
