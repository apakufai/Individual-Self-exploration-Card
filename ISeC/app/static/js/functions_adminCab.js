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