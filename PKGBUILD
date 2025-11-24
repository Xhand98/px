pkgname=px-cli
_pkgname=px       # nombre REAL del repo
pkgver=0.1.0
pkgrel=1
pkgdesc="AI-powered shell command generator"
arch=('any')
url="https://github.com/Xhand98/px"
license=('MIT')
depends=('python' 'python-openai' 'python-rich' 'python-dotenv')
makedepends=('python-build' 'python-installer' 'python-wheel' 'python-setuptools')
source=("$pkgname-$pkgver.tar.gz::$url/archive/refs/tags/v$pkgver.tar.gz")
sha256sums=('SKIP')

build() {
    cd "$_pkgname-$pkgver"
    python -m build --wheel --no-isolation
}

package() {
    cd "$_pkgname-$pkgver"
    python -m installer --destdir="$pkgdir" dist/*.whl
}
