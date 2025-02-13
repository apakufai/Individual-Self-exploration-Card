// Переход на другую страницу
function nextPage(constToHide, fromBlock, toPage) {
    const from = document.querySelector(fromBlock);
    from.classList.add('animBlockDisappear_end');
    from.addEventListener('animationend', function handler() {
        from.style.display = 'none';
        from.classList.remove('animBlockDisappear_end');
        constToHide.forEach(obj => {
            obj.style.display = 'none'; // Скрываем каждый элемент
        });
        // Переход на новую страницу после окончания анимации
        window.location.href = toPage;
        from.removeEventListener('animationend', handler);
    });
}

// Переход от описания блока к тестовым вопросам
function flipDescrToQuest(fromBlock, toBlock) {
    const from = document.querySelector(fromBlock);
    const to = document.querySelector(toBlock);
    from.classList.add('animBlockDisappear_next');
    from.addEventListener('animationend', function handler() {
        from.style.display = 'none';
        from.classList.remove('animBlockDisappear_next'); // Удаляем класс анимации
        to.style.display = 'block';
        to.classList.add('animBlockAppear_next');
        to.addEventListener('animationend', function appearHandler() {
            to.classList.remove('animBlockAppear_next'); // Удаляем класс анимации
            to.removeEventListener('animationend', appearHandler);
        });
        from.removeEventListener('animationend', handler);
    });
}

// Перелистывание вперед между блоками на одной странице
function flipFront(fromBlock, toBlock) {
    const from = document.querySelector(fromBlock);
    const to = document.querySelector(toBlock);
    from.classList.add('animBlockDisappear_next');
    from.addEventListener('animationend', function handler() {
        from.style.display = 'none';
        from.classList.remove('animBlockDisappear_next');
        to.style.display = 'block';
        to.classList.add('animBlockAppear_next');
        to.addEventListener('animationend', function appearHandler() {
            to.classList.remove('animBlockAppear_next');
            to.removeEventListener('animationend', appearHandler);
        });
        from.removeEventListener('animationend', handler);
    });
}

// Перелистывание назад от первого вопроса блока к описанию блока
function flipQuestToDescr(fromBlock, toBlock) {
    const from = document.querySelector(fromBlock);
    const to = document.querySelector(toBlock);
    from.classList.add('animBlockDisappear_prev');
    from.addEventListener('animationend', function handler() {
        from.style.display = 'none';
        from.classList.remove('animBlockDisappear_prev'); // Удаляем класс анимации
        to.style.display = 'block'; // Просто показываем элемент без анимации
        from.removeEventListener('animationend', handler);
    });
}

// Перелистывание назад между блоками на одной странице
function flipBack(fromBlock, toBlock) {
    const from = document.querySelector(fromBlock);
    const to = document.querySelector(toBlock);
    from.classList.add('animBlockDisappear_prev');
    from.addEventListener('animationend', function handler() {
        from.style.display = 'none';
        from.classList.remove('animBlockDisappear_prev'); // Удаляем класс анимации
        to.style.display = 'block';
        to.classList.add('animBlockAppear_prev'); // Добавляем класс анимации для появления
        to.addEventListener('animationend', function appearHandler() {
            to.classList.remove('animBlockAppear_prev'); // Удаляем класс анимации
            to.removeEventListener('animationend', appearHandler);
        });
        from.removeEventListener('animationend', handler);
    });
}

// Генерация случайного id
function generateRandomID(length) {
    let result = '';
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const charactersLength = characters.length;
    for (let i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}

// Создание id с проверкой на наличие в базе данных
async function generateUniqueId() {
    let isIdFree = false; // Счётчик проверки на существование id в базе
    let IdToCheck; // Объявляем переменную для ID

    do {
        IdToCheck = generateRandomID(8); // Сгенерированный id
        // Отправляем запрос на сервер для проверки id
        const response = await fetch('/check_user_id', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ userId: IdToCheck }) // Передаем JSON
        });
        const data = await response.json();
        if (data.error === 'connect_error') {
            alert('Ошибка подключения к базе данных.'); // Сообщение об ошибке подключения
            return null; // Выход из функции при ошибке
        }
        if (data.found) {
        } else {
            isIdFree = true; // ID свободен
        }
    } while (!isIdFree);

    return IdToCheck; // Возвращаем уникальный ID
}

// Работа с кнопками выбора (блоки 1 и 2)
function crossButtonSelection(top_0, top_1, top_2, top_3, bottom_0, bottom_1, bottom_2, bottom_3) {
    document.getElementById(top_0).addEventListener('change', function () {
        if (this.checked) {
            document.getElementById(bottom_3).checked = true;
        }
    });
    document.getElementById(top_1).addEventListener('change', function () {
        if (this.checked) {
            document.getElementById(bottom_2).checked = true;
        }
    });
    document.getElementById(top_2).addEventListener('change', function () {
        if (this.checked) {
            document.getElementById(bottom_1).checked = true;
        }
    });
    document.getElementById(top_3).addEventListener('change', function () {
        if (this.checked) {
            document.getElementById(bottom_0).checked = true;
        }
    });
    document.getElementById(bottom_3).addEventListener('change', function () {
        if (this.checked) {
            document.getElementById(top_0).checked = true;
        }
    });
    document.getElementById(bottom_2).addEventListener('change', function () {
        if (this.checked) {
            document.getElementById(top_1).checked = true;
        }
    });
    document.getElementById(bottom_1).addEventListener('change', function () {
        if (this.checked) {
            document.getElementById(top_2).checked = true;
        }
    });
    document.getElementById(bottom_0).addEventListener('change', function () {
        if (this.checked) {
            document.getElementById(top_3).checked = true;
        }
    });
}

// Работа с ползунками (блоки 3 и 5)
function threeSliders(slide1, slide2, slide3) {
    const value1 = parseInt(document.getElementById(slide1).querySelector('.slider').value, 10);
    const value2 = parseInt(document.getElementById(slide2).querySelector('.slider').value, 10);
    const value3 = parseInt(document.getElementById(slide3).querySelector('.slider').value, 10);
    return [value1, value2, value3];
}

// Работа с ползунками (блок 6)
function fourSliders(slide1, slide2, slide3, slide4) {
    const value1 = parseInt(document.getElementById(slide1).querySelector('.slider_6').value, 10);
    const value2 = parseInt(document.getElementById(slide2).querySelector('.slider_6').value, 10);
    const value3 = parseInt(document.getElementById(slide3).querySelector('.slider_6').value, 10);
    const value4 = parseInt(document.getElementById(slide4).querySelector('.slider_6').value, 10);
    return [value1, value2, value3, value4];
}

