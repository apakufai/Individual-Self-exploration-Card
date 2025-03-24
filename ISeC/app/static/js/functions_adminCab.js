// Генерация случайного id
function cab_generateRandomID(prefix, length) {
    let result = prefix;
    const characters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789';
    const charactersLength = characters.length;
    for (let i = 0; i < length; i++) {
        result += characters.charAt(Math.floor(Math.random() * charactersLength));
    }
    return result;
}



// --- СТРАНИЦА АРХИВА ---



function generAndSendPDF() {

    const respondentId = document.getElementById('respondent_id').value.trim();
    const emailToSend = document.getElementById('email_to_send').value.trim();

    const inputHandlerId = document.getElementById('respondent_id');
    inputHandlerId.value = respondentId;
    const inputHandlerEmail = document.getElementById('email_to_send');
    inputHandlerEmail.value = emailToSend;

    if (!respondentId) {
        alert("Введите ID респондента");
        return;
    }

    if (!emailToSend) {
        alert("Введите e-mail для отправки");
        return;
    }

    const emailPattern = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$/;
    if (!emailPattern.test(emailToSend)) {
        alert("E-mail некорректен");
        return;
    }

    // Диалоговое окно подтверждения
    if (confirm('Данные введены верно?')) {

        // Проверяем существующие respondentId
        let respondents = JSON.parse(localStorage.getItem('respondents')) || [];

        // Находим respondentId и его срок действия
        const existingRespondent = respondents.find(r => r.id === respondentId);
        const currentTime = Date.now();
        const expirationTime = existingRespondent ? existingRespondent.expiration : null;

        if (existingRespondent && currentTime < expirationTime) {
            const remainingTime = Math.ceil((expirationTime - currentTime) / 1000); // Оставшееся время в секундах
            alert(`Генерация данного ИКС-файла будет доступна через ${remainingTime} секунд`);
            return; // Выход из функции, если respondentId уже существует
        }

        // Отправка email на сервер для сохранения
        fetch('/cab_add_resend', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ email: emailToSend })
        })
            .then(response => response.text())  // Возвращается текстовый ответ

            // .then(text => {
            // 	console.log(text);  // Текст выводится в консоль
            // })

            .catch(error => {
                console.error('Ошибка:', error);
                alert('Произошла ошибка. Пожалуйста, обратитесь к администратору.');
            })
            .finally(() => {

                // Отправка данных на сервер
                fetch('/cab_get_respondent_data', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify({ userId: respondentId })
                })
                    .then(response => {
                        if (response.status === 404) {
                            alert("Такого id нет в базе данных");
                            return Promise.reject(); // Останавливаем выполнение
                        }

                        if (!response.ok) {
                            throw new Error('Ошибка при получении данных респондента');
                        }

                        return response.json();
                    })
                    .then(respondentData => {

                        // Создаем JSON-объект для хранения данных
                        const ISeC_results = {

                            downloadToPC: false,
                            receiveByEmail: true,
                            insertData: false,
                            emailToSend: emailToSend,

                            userGroup: respondentData.userGroup,
                            userId: respondentId,
                            userName: respondentData.userName,
                            userSurname: respondentData.userSurname,
                            userSex: respondentData.userSex,
                            userBirthyear: respondentData.userBirthyear,
                            userCategory: respondentData.userCategory,
                            userEmail: respondentData.userEmail,

                            adaptation_1: respondentData.adaptation_1,
                            compromise_1: respondentData.compromise_1,
                            bidding_1: respondentData.bidding_1,
                            threat_1: respondentData.threat_1,
                            logicArgument_1: respondentData.logicArgument_1,
                            emotionsArgument_1: respondentData.emotionsArgument_1,
                            adaptationCount_1: respondentData.adaptationCount_1,
                            compromiseCount_1: respondentData.compromiseCount_1,
                            biddingCount_1: respondentData.biddingCount_1,
                            threatCount_1: respondentData.threatCount_1,
                            logicArgumentCount_1: respondentData.logicArgumentCount_1,
                            emotionsArgumentCount_1: respondentData.emotionsArgumentCount_1,

                            b1_q1_top: respondentData.b1_q1_top,
                            b1_q2_top: respondentData.b1_q2_top,
                            b1_q3_top: respondentData.b1_q3_top,
                            b1_q4_top: respondentData.b1_q4_top,
                            b1_q5_top: respondentData.b1_q5_top,
                            b1_q6_top: respondentData.b1_q6_top,
                            b1_q7_top: respondentData.b1_q7_top,
                            b1_q8_top: respondentData.b1_q8_top,
                            b1_q9_top: respondentData.b1_q9_top,
                            b1_q10_top: respondentData.b1_q10_top,
                            b1_q11_top: respondentData.b1_q11_top,
                            b1_q12_top: respondentData.b1_q12_top,
                            b1_q13_top: respondentData.b1_q13_top,
                            b1_q14_top: respondentData.b1_q14_top,
                            b1_q15_top: respondentData.b1_q15_top,

                            adaptation_2: respondentData.adaptation_2,
                            compromise_2: respondentData.compromise_2,
                            threat_2: respondentData.threat_2,
                            cooperation_2: respondentData.cooperation_2,
                            avoidance_2: respondentData.avoidance_2,
                            adaptationCount_2: respondentData.adaptationCount_2,
                            compromiseCount_2: respondentData.compromiseCount_2,
                            threatCount_2: respondentData.threatCount_2,
                            cooperationCount_2: respondentData.cooperationCount_2,
                            avoidanceCount_2: respondentData.avoidanceCount_2,

                            b2_q1_top: respondentData.b2_q1_top,
                            b2_q2_top: respondentData.b2_q2_top,
                            b2_q3_top: respondentData.b2_q3_top,
                            b2_q4_top: respondentData.b2_q4_top,
                            b2_q5_top: respondentData.b2_q5_top,
                            b2_q6_top: respondentData.b2_q6_top,
                            b2_q7_top: respondentData.b2_q7_top,
                            b2_q8_top: respondentData.b2_q8_top,
                            b2_q9_top: respondentData.b2_q9_top,
                            b2_q10_top: respondentData.b2_q10_top,
                            b2_q11_top: respondentData.b2_q11_top,
                            b2_q12_top: respondentData.b2_q12_top,
                            b2_q13_top: respondentData.b2_q13_top,
                            b2_q14_top: respondentData.b2_q14_top,
                            b2_q15_top: respondentData.b2_q15_top,
                            b2_q16_top: respondentData.b2_q16_top,
                            b2_q17_top: respondentData.b2_q17_top,
                            b2_q18_top: respondentData.b2_q18_top,
                            b2_q19_top: respondentData.b2_q19_top,
                            b2_q20_top: respondentData.b2_q20_top,
                            b2_q21_top: respondentData.b2_q21_top,
                            b2_q22_top: respondentData.b2_q22_top,
                            b2_q23_top: respondentData.b2_q23_top,
                            b2_q24_top: respondentData.b2_q24_top,
                            b2_q25_top: respondentData.b2_q25_top,
                            b2_q26_top: respondentData.b2_q26_top,
                            b2_q27_top: respondentData.b2_q27_top,
                            b2_q28_top: respondentData.b2_q28_top,
                            b2_q29_top: respondentData.b2_q29_top,
                            b2_q30_top: respondentData.b2_q30_top,

                            adaptation_3: respondentData.adaptation_3,
                            threat_3: respondentData.threat_3,
                            cooperation_3: respondentData.cooperation_3,
                            adaptationCount_3: respondentData.adaptationCount_3,
                            threatCount_3: respondentData.threatCount_3,
                            cooperationCount_3: respondentData.cooperationCount_3,

                            b3_q1: respondentData.b3_q1,
                            b3_q2: respondentData.b3_q2,
                            b3_q3: respondentData.b3_q3,
                            b3_q4: respondentData.b3_q4,
                            b3_q5: respondentData.b3_q5,
                            b3_q6: respondentData.b3_q6,
                            b3_q7: respondentData.b3_q7,
                            b3_q8: respondentData.b3_q8,
                            b3_q9: respondentData.b3_q9,

                            understandingOfStyles_4: respondentData.understandingOfStyles_4,
                            strengthInstallation_4: respondentData.strengthInstallation_4,
                            manipulationInstallation_4: respondentData.manipulationInstallation_4,
                            negotiationsInstallation_4: respondentData.negotiationsInstallation_4,
                            strengthInstallationCount_4: respondentData.strengthInstallationCount_4,
                            manipulationInstallationCount_4: respondentData.manipulationInstallationCount_4,
                            negotiationsInstallationCount_4: respondentData.negotiationsInstallationCount_4,

                            b4_q1: respondentData.b4_q1,
                            b4_q2: respondentData.b4_q2,
                            b4_q3: respondentData.b4_q3,
                            b4_q4: respondentData.b4_q4,
                            b4_q5: respondentData.b4_q5,
                            b4_q6: respondentData.b4_q6,
                            b4_q7: respondentData.b4_q7,
                            b4_q8: respondentData.b4_q8,
                            b4_q9: respondentData.b4_q9,
                            b4_q10: respondentData.b4_q10,
                            b4_q11: respondentData.b4_q11,
                            b4_q12: respondentData.b4_q12,
                            b4_q13: respondentData.b4_q13,
                            b4_q14: respondentData.b4_q14,
                            b4_q15: respondentData.b4_q15,
                            b4_q16: respondentData.b4_q16,

                            adaptation_5: respondentData.adaptation_5,
                            bidding_5: respondentData.bidding_5,
                            logicArgument_5: respondentData.logicArgument_5,
                            emotionsArgument_5: respondentData.emotionsArgument_5,
                            avoidance_5: respondentData.avoidance_5,
                            adaptationCount_5: respondentData.adaptationCount_5,
                            biddingCount_5: respondentData.biddingCount_5,
                            logicArgumentCount_5: respondentData.logicArgumentCount_5,
                            emotionsArgumentCount_5: respondentData.emotionsArgumentCount_5,
                            avoidanceCount_5: respondentData.avoidanceCount_5,

                            b5_q1: respondentData.b5_q1,
                            b5_q2: respondentData.b5_q2,
                            b5_q3: respondentData.b5_q3,
                            b5_q4: respondentData.b5_q4,
                            b5_q5: respondentData.b5_q5,
                            b5_q6: respondentData.b5_q6,
                            b5_q7: respondentData.b5_q7,
                            b5_q8: respondentData.b5_q8,
                            b5_q9: respondentData.b5_q9,
                            b5_q10: respondentData.b5_q10,
                            b5_q11: respondentData.b5_q11,
                            b5_q12: respondentData.b5_q12,

                            logicArgument_6: respondentData.logicArgument_6,
                            emotionsArgument_6: respondentData.emotionsArgument_6,
                            logicArgumentCount_6: respondentData.logicArgumentCount_6,
                            emotionsArgumentCount_6: respondentData.emotionsArgumentCount_6,

                            b6_q1: respondentData.b6_q1,
                            b6_q2: respondentData.b6_q2,
                            b6_q3: respondentData.b6_q3,
                            b6_q4: respondentData.b6_q4,
                            b6_q5: respondentData.b6_q5,
                            b6_q6: respondentData.b6_q6,
                            b6_q7: respondentData.b6_q7,
                            b6_q8: respondentData.b6_q8,
                            b6_q9: respondentData.b6_q9,
                            b6_q10: respondentData.b6_q10
                        };

                        if (ISeC_results) { // Проверка существования данных

                            // Если respondentId не существует или срок действия истек, обновляем или добавляем его
                            const newExpirationTime = currentTime + 5 * 60 * 1000; // 5 минут в миллисекундах
                            if (existingRespondent) {
                                existingRespondent.expiration = newExpirationTime; // Обновляем срок действия
                            } else {
                                respondents.push({ id: respondentId, expiration: newExpirationTime }); // Добавляем новый respondentId
                            }

                            // Сохраняем обновленный массив в localStorage
                            localStorage.setItem('respondents', JSON.stringify(respondents));

                            alert("Генерация и отправка запущены успешно. Повторная отправка данного ИКС-файла будет возможна через 5 минут");

                            // Очистка полей ввода
                            inputHandlerId.value = '';
                            inputHandlerEmail.value = '';

                            fetch('/generate_and_download_pdf', {
                                method: 'POST',
                                headers: {
                                    'Content-Type': 'application/json'
                                },
                                body: JSON.stringify(ISeC_results)
                            })
                                .then(response => {
                                    if (!response.ok) {
                                        throw new Error('Ошибка при генерации и отправке PDF');
                                    }
                                    return response.blob();
                                })
                                .catch(error => {
                                    console.error('Ошибка:', error);
                                    alert('Произошла ошибка. Обратитесь к администратору');
                                });
                        } else {
                            console.error('Данные для генерации отсутствуют, или загрузка уже идет');
                        }
                    })
                    .catch(error => {
                        // Обрабатываем только те ошибки, которые не связаны с 404
                        if (error) {
                            console.error('Произошла ошибка:', error);
                            alert('Произошла ошибка. Пожалуйста, обратитесь к администратору.');
                        }
                    });
            });
    }
}



// --- СТРАНИЦА КОДОВ ДОСТУПА ---



// Создание id кода доступа с проверкой на наличие в базе данных
async function cab_generateUniqueCodeId() {
    let isIdFree = false; // Счётчик проверки на существование id в базе
    let IdToCheck; // Объявляем переменную для ID

    do {
        IdToCheck = cab_generateRandomID("code_", 4); // Сгенерированный id
        // Отправляем запрос на сервер для проверки id
        const response = await fetch('/cab_check_code_id', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ codeId: IdToCheck }) // Передаем JSON
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

// Создание строк таблицы кодов доступа
async function createCode(button) {
    const row = button.closest('tr');
    const codeId = await cab_generateUniqueCodeId();
    const currentDate = new Date();  // Получаем текущую дату
    const day = String(currentDate.getDate()).padStart(2, '0');
    const month = String(currentDate.getMonth() + 1).padStart(2, '0');
    const year = currentDate.getFullYear();
    const testGroupPart1 = `${day}.${month}.${year}`; // Форматируем дату в "DD.MM.YYYY"
    const testGroupPart2 = row.querySelector('input[name="test_group"]').value.trim();
    const testGroup = `${testGroupPart1} ${testGroupPart2}`.trim();
    const code = row.querySelector('input[name="code"]').value.trim();
    const startDate = row.querySelector('input[name="start_date"]').value;
    const endDate = row.querySelector('input[name="end_date"]').value;
    // Ожидание результата проверки вводимых данных
    const { hasErrors, errorList } = await validateCodeInputs("create", codeId, testGroup, testGroupPart2, code, startDate, endDate);
    if (hasErrors) {
        alert(errorList.join('\n'));  // Выводим ошибки
    } else {
        fetch('/cab_create_code', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                code_id: codeId,
                test_group: testGroup,
                code: code,
                start_date: startDate,
                end_date: endDate
            }),
            credentials: 'same-origin'  // Защита запросов от CSRF-атак
        })
            .then(response => {
                if (response.ok) {
                    location.reload();
                } else {
                    alert('Ошибка при создании');
                }
            })
            .catch(error => {
                console.error('Ошибка:', error);
            });
    }
}

// Изменение строк таблицы кодов доступа
async function updateCode(button) {
    const row = button.closest('tr');
    const codeId = button.getAttribute('code_id');
    const testGroupPart1 = row.querySelector('.entrycode_block_td_0').textContent.trim();
    const testGroupPart2 = row.querySelector('input[name="test_group"]').value.trim();
    const testGroup = `${testGroupPart1} ${testGroupPart2}`;
    const code = row.querySelector('input[name="code"]').value.trim();
    const startDate = row.querySelector('input[name="start_date"]').value;
    const endDate = row.querySelector('input[name="end_date"]').value;
    // Ожидание результата проверки вводимых данных
    const { hasErrors, errorList } = await validateCodeInputs("upadte", codeId, testGroup, testGroupPart2, code, startDate, endDate);
    if (hasErrors) {
        alert(errorList.join('\n'));  // Выводим ошибки
    } else {
        if (confirmUpdateCode()) {
            fetch(`/cab_update_code/${codeId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    test_group: testGroup,
                    code: code,
                    start_date: startDate,
                    end_date: endDate
                }),
                credentials: 'same-origin'  // Защита запросов от CSRF-атак
            })
                .then(response => {
                    if (response.ok) {
                        location.reload();
                    } else {
                        alert('Ошибка при обновлении');
                    }
                })
                .catch(error => {
                    console.error('Ошибка:', error);
                });
        }
    }
}

// Функция проверки данных кода доступа на валидность
async function validateCodeInputs(action, codeId, testGroup, testGroupPart2, code, startDate, endDate) {
    let hasErrors = false;
    let errorList = [];
    // Проверка на пустое название группы
    if (!testGroupPart2) {
        hasErrors = true;
        errorList.push("- Название группы не должно быть пустым");
    }
    // Проверка на пустой код
    if (!code) {
        hasErrors = true;
        errorList.push("- Поле кода доступа не должно быть пустым");
    }
    // Проверка на существование группы и кода в базе данных
    try {
        const response = await fetch('/cab_check_code', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ action: action, codeId: codeId, testGroup: testGroup, code: code }),
        });
        if (!response.ok) {
            throw new Error('Ошибка сети');
        }
        const checkResult = await response.json();
        if (checkResult.isGroupInDB) {
            hasErrors = true;
            errorList.push("- Такая группа уже существует");
        }
        if (checkResult.isCodeInDB) {
            hasErrors = true;
            errorList.push("- Такой код доступа уже существует");
        }
    } catch (error) {
        console.error('Ошибка:', error);
        hasErrors = true;
        errorList.push("- Ошибка проверки данных в базе");
    }
    // Проверка на пустые поля дат
    if (!startDate) {
        hasErrors = true;
        errorList.push("- Поле ввода даты ОТ пустое либо некорректное");
    }
    if (!endDate) {
        hasErrors = true;
        errorList.push("- Поле ввода даты ДО пустое либо некорректное");
    }
    // Проверка на корректность дат
    if (new Date(startDate) > new Date(endDate)) {
        hasErrors = true;
        errorList.push("- Дата ОТ позднее, чем дата ДО");
    }
    if (new Date(endDate) < new Date()) {
        hasErrors = true;
        errorList.push("- Дата ДО уже прошла");
    }
    // Возвращаем результат проверки и список ошибок
    return { hasErrors, errorList };
}

// Удаление строк таблицы кодов доступа
function deleteCode(button) {
    const codeId = button.getAttribute('code_id');
    const testGroup = button.getAttribute('test_group');
    if (confirmDeleteCode(testGroup)) {
        fetch(`/cab_delete_code/${codeId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            credentials: 'same-origin'  // Защита запросов от CSRF-атак
        })
            .then(response => {
                if (response.ok) {
                    location.reload();
                } else {
                    alert('Ошибка при удалении');
                }
            })
            .catch(error => {
                console.error('Ошибка:', error);
            });
    }
}



// --- СТРАНИЦА ГЕНЕРАЦИИ EXCEL-ФАЙЛА ---



function startExcelgen() {
    if (confirmExcelgen()) {
        const selectedGroups = Array.from(document.querySelectorAll('input[name="group_checkbox"]:checked')).map(el => el.value);
        const selectedCategories = Array.from(document.querySelectorAll('input[name="category_checkbox"]:checked')).map(el => el.value);
        const selectedSex = document.querySelector('input[name="sex"]:checked')?.value || null;
        const yearFrom = parseInt(document.getElementById('yearFrom').value, 10);
        const yearUntil = parseInt(document.getElementById('yearUntil').value, 10);

        // Проверяем, что yearFrom не больше yearUntil
        if (yearFrom > yearUntil) {
            alert("Год ОТ больше года ДО");
            return; // Прерываем выполнение функции
        }

        fetch('/cab_generate_query', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ groups: selectedGroups, categories: selectedCategories, sex: selectedSex, yearFrom, yearUntil })
        })
            .then(response => {
                if (response.ok) {
                    return response.blob().then(blob => {
                        const contentDisposition = response.headers.get('Content-Disposition');
                        const originalFilename = contentDisposition.match(/filename[^;=\n]*=((['"]).*?\2|[^;\n]*)/)?.[1]?.replace(/['"]/g, '') || 'download.xlsx';
                        const filename = `Запрос${originalFilename}`;

                        const url = window.URL.createObjectURL(blob);
                        const a = document.createElement('a');
                        a.style.display = 'none';
                        a.href = url;
                        a.download = filename;
                        document.body.appendChild(a);
                        a.click();
                        window.URL.revokeObjectURL(url);
                    });
                } else if (response.status === 404) {
                    return response.json().then(data => {
                        alert(data.error); // Показываем сообщение об ошибке
                    });
                } else {
                    throw new Error('Сетевой ответ не в порядке');
                }
            })
            .catch(console.error);

    }
}



// --- СТРАНИЦА АДМИНИСТРАТОРОВ ---



// Создание id администратора с проверкой на наличие в базе данных
async function cab_generateUniqueAdminId() {
    let isLoginFree = false; // Счётчик проверки на существование id в базе
    let loginToCheck; // Объявляем переменную для ID

    do {
        loginToCheck = cab_generateRandomID("admin_", 4); // Сгенерированный id
        // Отправляем запрос на сервер для проверки id
        const response = await fetch('/cab_check_admin_id', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ adminLogin: loginToCheck }) // Передаем JSON
        });
        const data = await response.json();
        if (data.error === 'connect_error') {
            alert('Ошибка подключения к базе данных.'); // Сообщение об ошибке подключения
            return null; // Выход из функции при ошибке
        }
        if (data.found) {
        } else {
            isLoginFree = true; // ID свободен
        }
    } while (!isLoginFree);

    return loginToCheck; // Возвращаем уникальный ID
}

// Создание строк таблицы администраторов
async function createAdmin(button) {
    const row = button.closest('tr');
    const adminId = await cab_generateUniqueAdminId();
    const login = row.querySelector('input[name="login"]').value.trim();
    const password = row.querySelector('input[name="password"]').value.trim();
    const confirmPassword = row.querySelector('input[name="confirm_password"]').value.trim();
    const adminName = row.querySelector('input[name="admin_name"]').value.trim();
    const archiveAccess = row.querySelector('input[name="archive_access_create"]').checked ? "true" : "false";
    const codesAccess = row.querySelector('input[name="codes_access_create"]').checked ? "true" : "false";
    const analysisAccess = row.querySelector('input[name="analysis_access_create"]').checked ? "true" : "false";
    const excelgenAccess = row.querySelector('input[name="excelgen_access_create"]').checked ? "true" : "false";
    const startDate = row.querySelector('input[name="start_date"]').value;
    const endDate = row.querySelector('input[name="end_date"]').value;
    // Ожидание результата проверки вводимых данных
    const { hasErrors, errorList } = await validateAdminInputs("create", adminId, login, password, confirmPassword, adminName, startDate, endDate);
    if (hasErrors) {
        alert(errorList.join('\n'));  // Выводим ошибки
    } else {
        fetch('/cab_create_admin', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                admin_id: adminId,
                login: login,
                password: password,
                admin_name: adminName,
                archive_access: archiveAccess,
                codes_access: codesAccess,
                analysis_access: analysisAccess,
                excelgen_access: excelgenAccess,
                start_date: startDate,
                end_date: endDate
            }),
            credentials: 'same-origin'  // Защита запросов от CSRF-атак
        })
            .then(response => {
                if (response.ok) {
                    location.reload();
                } else {
                    alert('Ошибка при создании');
                }
            })
            .catch(error => {
                console.error('Ошибка:', error);
            });
    }
}

// Изменение строк таблицы администраторов
async function updateAdmin(button) {
    const row = button.closest('tr');
    const adminId = button.getAttribute('admin_id');
    const login = row.querySelector('input[name="login"]').value.trim();
    const password = row.querySelector('input[name="password"]').value.trim();
    const confirmPassword = row.querySelector('input[name="confirm_password"]').value.trim();
    const passwordToSend = (password && confirmPassword) ? password : null; // Если оба поля пароля пустые, отправляем null
    const adminName = row.querySelector('input[name="admin_name"]').value.trim();
    const archiveAccess = row.querySelector('input[id="archive_access"]').checked ? "true" : "false";
    const codesAccess = row.querySelector('input[id="codes_access"]').checked ? "true" : "false";
    const analysisAccess = row.querySelector('input[id="analysis_access"]').checked ? "true" : "false";
    const excelgenAccess = row.querySelector('input[id="excelgen_access"]').checked ? "true" : "false";
    const startDate = row.querySelector('input[name="start_date"]').value;
    const endDate = row.querySelector('input[name="end_date"]').value;
    // Ожидание результата проверки вводимых данных
    const { hasErrors, errorList } = await validateAdminInputs("update", adminId, login, password, confirmPassword, adminName, startDate, endDate);
    if (hasErrors) {
        alert(errorList.join('\n'));  // Выводим ошибки
    } else {
        if (confirmUpdateAdmin()) {
            fetch(`/cab_update_admin/${adminId}`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    login: login,
                    password: passwordToSend,
                    admin_name: adminName,
                    archive_access: archiveAccess,
                    codes_access: codesAccess,
                    analysis_access: analysisAccess,
                    excelgen_access: excelgenAccess,
                    start_date: startDate,
                    end_date: endDate
                }),
                credentials: 'same-origin'  // Защита запросов от CSRF-атак
            })
                .then(response => {
                    if (response.ok) {
                        location.reload();
                    } else {
                        alert('Ошибка при обновлении');
                    }
                })
                .catch(error => {
                    console.error('Ошибка:', error);
                });
        }
    }
}

// Функция проверки данных администратора на валидность
async function validateAdminInputs(action, adminId, login, password, confirmPassword, adminName, startDate, endDate) {
    let hasErrors = false;
    let errorList = [];
    // Проверка на пустое поле и наличие недопустимых символов в логине администратора
    if (!login) {
        hasErrors = true;
        errorList.push("- Поле логина не должно быть пустым");
    } else if (!/^[а-яА-Яa-zA-Z0-9]+$/.test(login)) {
        hasErrors = true;
        errorList.push("- В логине администратора должны быть только буквы и цифры");
    }
    if (action === "create") {
        // Проверка на пустое поле пароля
        if (!password) {
            hasErrors = true;
            errorList.push("- Поле пароля не должно быть пустым");
        }
        // Проверка на пустое поле подтверждения пароля
        if (!confirmPassword) {
            hasErrors = true;
            errorList.push("- Поле подтверждения пароля не должно быть пустым");
        }
        // Проверка на совпадение паролей
        if (password && confirmPassword && (password !== confirmPassword)) {
            hasErrors = true;
            errorList.push("- Пароли не совпадают");
        }
    }
    if (action === "update") {
        if (password || confirmPassword) {
            // Проверка на пустое поле пароля
            if (!password) {
                hasErrors = true;
                errorList.push("- Поле пароля не должно быть пустым");
            }
            // Проверка на пустое поле подтверждения пароля
            if (!confirmPassword) {
                hasErrors = true;
                errorList.push("- Поле подтверждения пароля не должно быть пустым");
            }
            // Проверка на совпадение паролей
            if (password && confirmPassword && (password !== confirmPassword)) {
                hasErrors = true;
                errorList.push("- Пароли не совпадают");
            }
        }
    }
    // Проверка на пустое поле и наличие недопустимых символов в имени администратора
    if (!adminName) {
        hasErrors = true;
        errorList.push("- Поле имени администратора не должно быть пустым");
    } else if (!/^[а-яА-Яa-zA-Z]+( [а-яА-Яa-zA-Z]+)?$/.test(adminName)) {
        hasErrors = true;
        errorList.push("- В имени администратора должны быть только буквы и не более одного пробела");
    }
    // Проверка на существование логина и имени администратора в базе данных
    try {
        const response = await fetch('/cab_check_admin', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ action: action, adminId: adminId, login: login, adminName: adminName }),
        });
        if (!response.ok) {
            throw new Error('Ошибка сети');
        }
        const checkResult = await response.json();
        if (checkResult.isLoginInDB) {
            hasErrors = true;
            errorList.push("- Такой логин уже существует");
        }
        if (checkResult.isAdminNameInDB) {
            hasErrors = true;
            errorList.push("- Такое имя администратора уже существует");
        }
    } catch (error) {
        console.error('Ошибка:', error);
        hasErrors = true;
        errorList.push("- Ошибка проверки данных в базе");
    }
    // Проверка на пустые поля дат
    if (!startDate) {
        hasErrors = true;
        errorList.push("- Поле ввода даты ОТ пустое либо некорректное");
    }
    if (!endDate) {
        hasErrors = true;
        errorList.push("- Поле ввода даты ДО пустое либо некорректное");
    }
    // Проверка на корректность дат
    if (new Date(startDate) > new Date(endDate)) {
        hasErrors = true;
        errorList.push("- Дата ОТ позднее, чем дата ДО");
    }
    if (new Date(endDate) < new Date()) {
        hasErrors = true;
        errorList.push("- Дата ДО уже прошла");
    }
    // Возвращаем результат проверки и список ошибок
    return { hasErrors, errorList };
}

// Удаление строк таблицы администраторов
function deleteAdmin(button) {
    const adminId = button.getAttribute('admin_id');
    const adminLogin = button.getAttribute('login');
    const adminName = button.getAttribute('admin_name');
    if (confirmDeleteAdmin(adminName, adminLogin)) {
        fetch(`/cab_delete_admin/${adminId}`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            credentials: 'same-origin'  // Защита запросов от CSRF-атак
        })
            .then(response => {
                if (response.ok) {
                    location.reload();
                } else {
                    alert('Ошибка при удалении');
                }
            })
            .catch(error => {
                console.error('Ошибка:', error);
            });
    }
}

// Изменение строки главного администратора
async function updateMainAdmin(button) {
    const row = button.closest('tr');
    const login = row.querySelector('input[name="login"]').value.trim();
    const password = row.querySelector('input[name="password"]').value.trim();
    const confirmPassword = row.querySelector('input[name="confirm_password"]').value.trim();
    const passwordToSend = (password && confirmPassword) ? password : null; // Если оба поля пароля пустые, отправляем null
    const adminName = row.querySelector('input[name="admin_name"]').value.trim();
    // Ожидание результата проверки вводимых данных
    const { hasErrors, errorList } = await validateMainAdminInputs(login, password, confirmPassword, adminName);
    if (hasErrors) {
        alert(errorList.join('\n'));  // Выводим ошибки
    } else {
        if (confirmUpdateMainAdmin()) {
            fetch(`/cab_update_main_admin`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({
                    login: login,
                    password: passwordToSend,
                    admin_name: adminName
                }),
                credentials: 'same-origin'  // Защита запросов от CSRF-атак
            })
                .then(response => {
                    if (response.ok) {
                        location.reload();
                    } else {
                        alert('Ошибка при обновлении');
                    }
                })
                .catch(error => {
                    console.error('Ошибка:', error);
                });
        }
    }
}

// Функция проверки данных главного администратора на валидность
async function validateMainAdminInputs(login, password, confirmPassword, adminName) {
    let hasErrors = false;
    let errorList = [];
    // Проверка на пустое поле и наличие недопустимых символов в логине администратора
    if (!login) {
        hasErrors = true;
        errorList.push("- Поле логина не должно быть пустым");
    } else if (!/^[а-яА-Яa-zA-Z0-9]+$/.test(login)) {
        hasErrors = true;
        errorList.push("- В логине администратора должны быть только буквы и цифры");
    }
    if (password || confirmPassword) {
        // Проверка на пустое поле пароля
        if (!password) {
            hasErrors = true;
            errorList.push("- Поле пароля не должно быть пустым");
        }
        // Проверка на пустое поле подтверждения пароля
        if (!confirmPassword) {
            hasErrors = true;
            errorList.push("- Поле подтверждения пароля не должно быть пустым");
        }
        // Проверка на совпадение паролей
        if (password && confirmPassword && (password !== confirmPassword)) {
            hasErrors = true;
            errorList.push("- Пароли не совпадают");
        }
    }
    // Проверка на пустое поле и наличие недопустимых символов в имени администратора
    if (!adminName) {
        hasErrors = true;
        errorList.push("- Поле имени администратора не должно быть пустым");
    } else if (!/^[а-яА-Яa-zA-Z]+( [а-яА-Яa-zA-Z]+)?$/.test(adminName)) {
        hasErrors = true;
        errorList.push("- В имени администратора должны быть только буквы и не более одного пробела");
    }
    // Проверка на существование логина и имени администратора в базе данных
    try {
        const response = await fetch('/cab_check_admin', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ action: "update", adminId: "admin", login: login, adminName: adminName }),
        });
        if (!response.ok) {
            throw new Error('Ошибка сети');
        }
        const checkResult = await response.json();
        if (checkResult.isLoginInDB) {
            hasErrors = true;
            errorList.push("- Такой логин уже существует");
        }
        if (checkResult.isAdminNameInDB) {
            hasErrors = true;
            errorList.push("- Такое имя администратора уже существует");
        }
    } catch (error) {
        console.error('Ошибка:', error);
        hasErrors = true;
        errorList.push("- Ошибка проверки данных в базе");
    }
    // Возвращаем результат проверки и список ошибок
    return { hasErrors, errorList };
}

// Функция скачивания электронных адресов из БД
function downloadEmailData() {
    if (confirmDownloadMailbase()) {
        fetch('/download_emaildata', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
        })
            .then(response => {
                if (!response.ok) {
                    return response.json().then(data => {
                        alert(data.message);
                    });
                }
                return response.blob(); // Получаем файл
            })
            .then(blob => {
                const url = window.URL.createObjectURL(blob);
                const a = document.createElement('a');
                a.href = url;
                a.download = 'База_адресов.txt'; // Имя файла для скачивания
                document.body.appendChild(a);
                a.click();
                a.remove();
            })
            .catch(error => console.error('Error:', error));
    }
}