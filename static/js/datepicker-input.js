// ページが読み込まれたときに実行される処理
document.addEventListener('DOMContentLoaded', function() {
    // 日付入力欄にイベントリスナーを追加
    const dateInputs = document.querySelectorAll('.datepicker-input');
    dateInputs.forEach(function(input) {
        input.addEventListener('change', function() {
            // カレンダーから選択された日付を取得
            const selectedDate = new Date(this.value);
            // 年/月/日形式で表示する
            if (!isNaN(selectedDate.getTime())) {
                this.value = formatDate(selectedDate);
            }
        });
    });

    // 日付のフォーマットを変換する関数
    function formatDate(date) {
        // 年、月、日を取得
        const year = date.getFullYear();
        const month = ('0' + (date.getMonth() + 1)).slice(-2); // 1桁の場合は0を追加
        const day = ('0' + date.getDate()).slice(-2); // 1桁の場合は0を追加
        // 年/月/日形式で返す
        return `${year}/${month}/${day}`;
    }
});

