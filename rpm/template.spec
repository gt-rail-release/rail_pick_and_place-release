Name:           ros-jade-rail-recognition
Version:        1.1.8
Release:        0%{?dist}
Summary:        ROS rail_recognition package

Group:          Development/Libraries
License:        BSD
URL:            http://ros.org/wiki/rail_recognition
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jade-actionlib
Requires:       ros-jade-actionlib-msgs
Requires:       ros-jade-cv-bridge
Requires:       ros-jade-geometry-msgs
Requires:       ros-jade-graspdb
Requires:       ros-jade-pcl-conversions
Requires:       ros-jade-pcl-ros
Requires:       ros-jade-rail-manipulation-msgs
Requires:       ros-jade-rail-pick-and-place-msgs
Requires:       ros-jade-rail-segmentation
Requires:       ros-jade-roscpp
Requires:       ros-jade-sensor-msgs
Requires:       ros-jade-std-msgs
Requires:       ros-jade-std-srvs
Requires:       ros-jade-tf2
BuildRequires:  ros-jade-actionlib
BuildRequires:  ros-jade-actionlib-msgs
BuildRequires:  ros-jade-catkin
BuildRequires:  ros-jade-cv-bridge
BuildRequires:  ros-jade-geometry-msgs
BuildRequires:  ros-jade-graspdb
BuildRequires:  ros-jade-pcl-conversions
BuildRequires:  ros-jade-pcl-ros
BuildRequires:  ros-jade-rail-manipulation-msgs
BuildRequires:  ros-jade-rail-pick-and-place-msgs
BuildRequires:  ros-jade-rail-segmentation
BuildRequires:  ros-jade-roscpp
BuildRequires:  ros-jade-sensor-msgs
BuildRequires:  ros-jade-std-msgs
BuildRequires:  ros-jade-std-srvs
BuildRequires:  ros-jade-tf2

%description
Construction and Use of a Recognition Database for Grasping Purposes

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
mkdir -p obj-%{_target_platform} && cd obj-%{_target_platform}
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/jade" \
        -DCMAKE_PREFIX_PATH="/opt/ros/jade" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jade/setup.sh" ]; then . "/opt/ros/jade/setup.sh"; fi
cd obj-%{_target_platform}
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/jade

%changelog
* Tue Aug 18 2015 David Kent <davidkent@wpi.edu> - 1.1.8-0
- Autogenerated by Bloom

* Fri May 08 2015 David Kent <davidkent@wpi.edu> - 1.1.7-0
- Autogenerated by Bloom

* Tue May 05 2015 David Kent <davidkent@wpi.edu> - 1.1.6-0
- Autogenerated by Bloom

* Mon May 04 2015 David Kent <davidkent@wpi.edu> - 1.1.5-0
- Autogenerated by Bloom

