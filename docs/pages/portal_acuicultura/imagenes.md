# El portal en imágenes

Este espacio visual complementa el Portal de Acuicultura con fotografías de formación, prácticas, instalaciones y actividades de articulación.

## Galería institucional

<style>
.gallery {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(250px, 1fr));
  gap: 20px;
  padding: 20px;
}

.gallery-item {
  position: relative;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.1);
  transition: transform 0.3s ease;
  cursor: pointer;
}

.gallery-item:hover {
  transform: scale(1.05);
  box-shadow: 0 8px 20px rgba(0, 0, 0, 0.15);
}

.gallery-item img {
  width: 100%;
  height: 250px;
  object-fit: cover;
  display: block;
}

.lightbox {
  display: none;
  position: fixed;
  z-index: 1000;
  left: 0;
  top: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, 0.9);
}

.lightbox.active {
  display: flex;
  align-items: center;
  justify-content: center;
}

.lightbox-content {
  max-width: 90%;
  max-height: 90%;
  position: relative;
}

.lightbox-content img {
  width: 100%;
  height: auto;
}

.lightbox-close {
  position: absolute;
  top: -40px;
  right: 0;
  color: white;
  font-size: 40px;
  font-weight: bold;
  cursor: pointer;
}

.lightbox-close:hover {
  color: #ccc;
}
</style>

<div class="gallery" id="gallery">
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/1 (2).jpeg" alt="Imagen 1">
  </a>
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/2 (2).jpeg" alt="Imagen 2">
  </a>
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/3.jpeg" alt="Imagen 3">
  </a>
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/4.jpeg" alt="Imagen 4">
  </a>
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/5.jpeg" alt="Imagen 5">
  </a>
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/6.jpeg" alt="Imagen 6">
  </a>
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/7.jpeg" alt="Imagen 7">
  </a>
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/8.jpeg" alt="Imagen 8">
  </a>
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/9.jpeg" alt="Imagen 9">
  </a>
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/10.jpeg" alt="Imagen 10">
  </a>
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/11.jpeg" alt="Imagen 11">
  </a>
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/12.jpeg" alt="Imagen 12">
  </a>
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/13.jpg" alt="Imagen 13">
  </a>
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/14.jpeg" alt="Imagen 14">
  </a>
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/15.jpeg" alt="Imagen 15">
  </a>
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/16.jpeg" alt="Imagen 16">
  </a>
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/17.jpg" alt="Imagen 17">
  </a>
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/18.jpg" alt="Imagen 18">
  </a>
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/19.jpg" alt="Imagen 19">
  </a>
  <a class="gallery-item" href="#" onclick="openLightbox(this); return false;">
    <img src="../images/20.jpg" alt="Imagen 20">
  </a>
</div>

<div class="lightbox" id="lightbox">
  <span class="lightbox-close" onclick="closeLightbox()">&times;</span>
  <div class="lightbox-content">
    <img id="lightbox-img" src="" alt="">
  </div>
</div>

<script>
function openLightbox(element) {
  const img = element.querySelector('img');
  document.getElementById('lightbox-img').src = img.src;
  document.getElementById('lightbox').classList.add('active');
}

function closeLightbox() {
  document.getElementById('lightbox').classList.remove('active');
}

document.getElementById('lightbox').addEventListener('click', function(e) {
  if (e.target === this) {
    closeLightbox();
  }
});
</script>

> Las imágenes mostradas documentan actividades de formación, prácticas de campo e instalaciones del portal de acuicultura de la FCyT UADER.

