
(cl:in-package :asdf)

(defsystem "minik_ros_wrapper-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "minikGetButtonMsg" :depends-on ("_package_minikGetButtonMsg"))
    (:file "_package_minikGetButtonMsg" :depends-on ("_package"))
    (:file "minikGetDistSensorMsg" :depends-on ("_package_minikGetDistSensorMsg"))
    (:file "_package_minikGetDistSensorMsg" :depends-on ("_package"))
    (:file "minikGetLedMsg" :depends-on ("_package_minikGetLedMsg"))
    (:file "_package_minikGetLedMsg" :depends-on ("_package"))
    (:file "minikGetLineFollowerSensorMsg" :depends-on ("_package_minikGetLineFollowerSensorMsg"))
    (:file "_package_minikGetLineFollowerSensorMsg" :depends-on ("_package"))
    (:file "minikGetPIDPositionMsg" :depends-on ("_package_minikGetPIDPositionMsg"))
    (:file "_package_minikGetPIDPositionMsg" :depends-on ("_package"))
    (:file "minikGetPIDVelocityMsg" :depends-on ("_package_minikGetPIDVelocityMsg"))
    (:file "_package_minikGetPIDVelocityMsg" :depends-on ("_package"))
    (:file "minikGetPositionMsg" :depends-on ("_package_minikGetPositionMsg"))
    (:file "_package_minikGetPositionMsg" :depends-on ("_package"))
    (:file "minikGetVelocityMsg" :depends-on ("_package_minikGetVelocityMsg"))
    (:file "_package_minikGetVelocityMsg" :depends-on ("_package"))
    (:file "minikSetConfigMsg" :depends-on ("_package_minikSetConfigMsg"))
    (:file "_package_minikSetConfigMsg" :depends-on ("_package"))
    (:file "minikSetLedMsg" :depends-on ("_package_minikSetLedMsg"))
    (:file "_package_minikSetLedMsg" :depends-on ("_package"))
    (:file "minikSetPIDPositionMsg" :depends-on ("_package_minikSetPIDPositionMsg"))
    (:file "_package_minikSetPIDPositionMsg" :depends-on ("_package"))
    (:file "minikSetPIDVelocityMsg" :depends-on ("_package_minikSetPIDVelocityMsg"))
    (:file "_package_minikSetPIDVelocityMsg" :depends-on ("_package"))
    (:file "minikSetPositionMsg" :depends-on ("_package_minikSetPositionMsg"))
    (:file "_package_minikSetPositionMsg" :depends-on ("_package"))
    (:file "minikSetVelocityMsg" :depends-on ("_package_minikSetVelocityMsg"))
    (:file "_package_minikSetVelocityMsg" :depends-on ("_package"))
    (:file "minikVelocitySetMsg" :depends-on ("_package_minikVelocitySetMsg"))
    (:file "_package_minikVelocitySetMsg" :depends-on ("_package"))
  ))