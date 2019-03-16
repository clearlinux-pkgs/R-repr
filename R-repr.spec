#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : R-repr
Version  : 0.19.2
Release  : 35
URL      : https://cran.r-project.org/src/contrib/repr_0.19.2.tar.gz
Source0  : https://cran.r-project.org/src/contrib/repr_0.19.2.tar.gz
Summary  : String and binary representations of objects for several formats / mime types
Group    : Development/Tools
License  : GPL-3.0
Requires: R-base64enc
Requires: R-htmltools
Requires: R-jsonlite
BuildRequires : R-base64enc
BuildRequires : R-htmltools
BuildRequires : R-jsonlite
BuildRequires : buildreq-R

%description
repr&emsp;[![b-Travis]][Travis] [![b-CRAN]][CRAN]
====
[b-Travis]: https://travis-ci.org/IRkernel/repr.svg?branch=master "Build status"
[Travis]: https://travis-ci.org/IRkernel/repr
[b-CRAN]: https://www.r-pkg.org/badges/version/repr "Comprehensive R Archive Network"
[CRAN]: https://cran.r-project.org/package=repr

%prep
%setup -q -c -n repr

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549468952

%install
export SOURCE_DATE_EPOCH=1549468952
rm -rf %{buildroot}
export LANG=C
export CFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FCFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export FFLAGS="$CFLAGS -O3 -flto -fno-semantic-interposition "
export CXXFLAGS="$CXXFLAGS -O3 -flto -fno-semantic-interposition "
export AR=gcc-ar
export RANLIB=gcc-ranlib
export LDFLAGS="$LDFLAGS  -Wl,-z -Wl,relro"
mkdir -p %{buildroot}/usr/lib64/R/library

mkdir -p ~/.R
mkdir -p ~/.stash
echo "CFLAGS = $CFLAGS -march=haswell -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=haswell -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library repr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx2 ; mv $i.avx2 ~/.stash/; done
echo "CFLAGS = $CFLAGS -march=skylake-avx512 -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -march=skylake-avx512 -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --no-test-load --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library repr
for i in `find %{buildroot}/usr/lib64/R/ -name "*.so"`; do mv $i $i.avx512 ; mv $i.avx512 ~/.stash/; done
echo "CFLAGS = $CFLAGS -ftree-vectorize " > ~/.R/Makevars
echo "FFLAGS = $FFLAGS -ftree-vectorize " >> ~/.R/Makevars
echo "CXXFLAGS = $CXXFLAGS -ftree-vectorize " >> ~/.R/Makevars
R CMD INSTALL --preclean --install-tests --built-timestamp=${SOURCE_DATE_EPOCH} --build  -l %{buildroot}/usr/lib64/R/library repr
cp ~/.stash/* %{buildroot}/usr/lib64/R/library/*/libs/ || :
%{__rm} -rf %{buildroot}%{_datadir}/R/library/R.css

%files
%defattr(-,root,root,-)
/usr/lib64/R/library/repr/DESCRIPTION
/usr/lib64/R/library/repr/INDEX
/usr/lib64/R/library/repr/Meta/Rd.rds
/usr/lib64/R/library/repr/Meta/features.rds
/usr/lib64/R/library/repr/Meta/hsearch.rds
/usr/lib64/R/library/repr/Meta/links.rds
/usr/lib64/R/library/repr/Meta/nsInfo.rds
/usr/lib64/R/library/repr/Meta/package.rds
/usr/lib64/R/library/repr/NAMESPACE
/usr/lib64/R/library/repr/NEWS.md
/usr/lib64/R/library/repr/R/repr
/usr/lib64/R/library/repr/R/repr.rdb
/usr/lib64/R/library/repr/R/repr.rdx
/usr/lib64/R/library/repr/help/AnIndex
/usr/lib64/R/library/repr/help/aliases.rds
/usr/lib64/R/library/repr/help/paths.rds
/usr/lib64/R/library/repr/help/repr.rdb
/usr/lib64/R/library/repr/help/repr.rdx
/usr/lib64/R/library/repr/html/00Index.html
/usr/lib64/R/library/repr/html/R.css
/usr/lib64/R/library/repr/tests/testthat.R
/usr/lib64/R/library/repr/tests/testthat/test_array_manipulation.r
/usr/lib64/R/library/repr/tests/testthat/test_escaping.r
/usr/lib64/R/library/repr/tests/testthat/test_repr_array_df.r
/usr/lib64/R/library/repr/tests/testthat/test_repr_htmlwidget.r
/usr/lib64/R/library/repr/tests/testthat/test_repr_list.r
/usr/lib64/R/library/repr/tests/testthat/test_repr_packageIQR.r
/usr/lib64/R/library/repr/tests/testthat/test_repr_vector.r
/usr/lib64/R/library/repr/tests/testthat/test_utils.r
