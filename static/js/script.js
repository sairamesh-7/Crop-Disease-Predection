<script>
console.log("AgriPredict loaded"); // ✅ check JS is running

const form = document.getElementById("uploadForm");
const loader = document.getElementById("loader");

form.addEventListener("submit", function(e){
    console.log("Form submitted"); // ✅ check click works

    loader.classList.add("active");

    document.querySelector(".main-btn").disabled = true;

    setTimeout(() => {
        form.submit();
    }, 300);

    e.preventDefault();
});
</script>