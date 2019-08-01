#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-nuiton
Version  : 1.3
Release  : 1
URL      : https://repo1.maven.org/maven2/org/nuiton/processor/nuiton-processor/1.3/nuiton-processor-1.3.jar
Source0  : https://repo1.maven.org/maven2/org/nuiton/processor/nuiton-processor/1.3/nuiton-processor-1.3.jar
Source1  : https://repo1.maven.org/maven2/org/nuiton/mavenpom/3.4.4/mavenpom-3.4.4.pom
Source2  : https://repo1.maven.org/maven2/org/nuiton/mavenpom4redmine/3.4.4/mavenpom4redmine-3.4.4.pom
Source3  : https://repo1.maven.org/maven2/org/nuiton/mavenpom4redmineAndCentral/3.4.4/mavenpom4redmineAndCentral-3.4.4.pom
Source4  : https://repo1.maven.org/maven2/org/nuiton/processor/1.3/processor-1.3.pom
Source5  : https://repo1.maven.org/maven2/org/nuiton/processor/nuiton-processor/1.3/nuiton-processor-1.3.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 LGPL-3.0 MIT
Requires: mvn-nuiton-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-nuiton package.
Group: Data

%description data
data components for the mvn-nuiton package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/nuiton/processor/nuiton-processor/1.3
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/nuiton/processor/nuiton-processor/1.3/nuiton-processor-1.3.jar

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/nuiton/mavenpom/3.4.4
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/nuiton/mavenpom/3.4.4/mavenpom-3.4.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/nuiton/mavenpom4redmine/3.4.4
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/nuiton/mavenpom4redmine/3.4.4/mavenpom4redmine-3.4.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/nuiton/mavenpom4redmineAndCentral/3.4.4
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/nuiton/mavenpom4redmineAndCentral/3.4.4/mavenpom4redmineAndCentral-3.4.4.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/nuiton/processor/1.3
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/nuiton/processor/1.3/processor-1.3.pom

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/nuiton/processor/nuiton-processor/1.3
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/nuiton/processor/nuiton-processor/1.3/nuiton-processor-1.3.pom


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/nuiton/mavenpom/3.4.4/mavenpom-3.4.4.pom
/usr/share/java/.m2/repository/org/nuiton/mavenpom4redmine/3.4.4/mavenpom4redmine-3.4.4.pom
/usr/share/java/.m2/repository/org/nuiton/mavenpom4redmineAndCentral/3.4.4/mavenpom4redmineAndCentral-3.4.4.pom
/usr/share/java/.m2/repository/org/nuiton/processor/1.3/processor-1.3.pom
/usr/share/java/.m2/repository/org/nuiton/processor/nuiton-processor/1.3/nuiton-processor-1.3.jar
/usr/share/java/.m2/repository/org/nuiton/processor/nuiton-processor/1.3/nuiton-processor-1.3.pom
