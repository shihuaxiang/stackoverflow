# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'stylewidget.ui'
#
# Created by: PyQt5 UI code generator 5.12.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_StyleWidget(object):
    def setupUi(self, StyleWidget):
        StyleWidget.setObjectName("StyleWidget")
        StyleWidget.resize(184, 245)
        self.gridLayout = QtWidgets.QGridLayout(StyleWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(StyleWidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_2.setContentsMargins(4, 4, 4, 4)
        self.gridLayout_2.setSpacing(4)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.transparentStyle = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.transparentStyle.sizePolicy().hasHeightForWidth())
        self.transparentStyle.setSizePolicy(sizePolicy)
        self.transparentStyle.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.transparentStyle.setCheckable(True)
        self.transparentStyle.setChecked(False)
        self.transparentStyle.setAutoExclusive(True)
        self.transparentStyle.setObjectName("transparentStyle")
        self.gridLayout_2.addWidget(self.transparentStyle, 0, 0, 1, 1)
        self.blueStyle = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.blueStyle.sizePolicy().hasHeightForWidth())
        self.blueStyle.setSizePolicy(sizePolicy)
        self.blueStyle.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.blueStyle.setCheckable(True)
        self.blueStyle.setChecked(False)
        self.blueStyle.setAutoExclusive(True)
        self.blueStyle.setObjectName("blueStyle")
        self.gridLayout_2.addWidget(self.blueStyle, 2, 0, 1, 1)
        self.khakiStyle = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.khakiStyle.sizePolicy().hasHeightForWidth())
        self.khakiStyle.setSizePolicy(sizePolicy)
        self.khakiStyle.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.khakiStyle.setCheckable(True)
        self.khakiStyle.setChecked(False)
        self.khakiStyle.setAutoExclusive(True)
        self.khakiStyle.setObjectName("khakiStyle")
        self.gridLayout_2.addWidget(self.khakiStyle, 0, 1, 1, 1)
        self.noStyle = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.noStyle.sizePolicy().hasHeightForWidth())
        self.noStyle.setSizePolicy(sizePolicy)
        self.noStyle.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.noStyle.setCheckable(True)
        self.noStyle.setChecked(True)
        self.noStyle.setAutoExclusive(True)
        self.noStyle.setObjectName("noStyle")
        self.gridLayout_2.addWidget(self.noStyle, 2, 1, 1, 1)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(4, 4, 4, 4)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(StyleWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.spinBox = QtWidgets.QSpinBox(StyleWidget)
        self.spinBox.setFocusPolicy(QtCore.Qt.WheelFocus)
        self.spinBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.spinBox.setKeyboardTracking(False)
        self.spinBox.setObjectName("spinBox")
        self.horizontalLayout.addWidget(self.spinBox)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 2)
        self.horizontalScrollBar = QtWidgets.QScrollBar(StyleWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalScrollBar.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar.setSizePolicy(sizePolicy)
        self.horizontalScrollBar.setMinimumSize(QtCore.QSize(0, 24))
        self.horizontalScrollBar.setFocusPolicy(QtCore.Qt.TabFocus)
        self.horizontalScrollBar.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar.setObjectName("horizontalScrollBar")
        self.gridLayout.addWidget(self.horizontalScrollBar, 3, 0, 1, 1)
        self.horizontalScrollBar_2 = QtWidgets.QScrollBar(StyleWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.horizontalScrollBar_2.sizePolicy().hasHeightForWidth())
        self.horizontalScrollBar_2.setSizePolicy(sizePolicy)
        self.horizontalScrollBar_2.setMinimumSize(QtCore.QSize(0, 24))
        self.horizontalScrollBar_2.setFocusPolicy(QtCore.Qt.TabFocus)
        self.horizontalScrollBar_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_2.setObjectName("horizontalScrollBar_2")
        self.gridLayout.addWidget(self.horizontalScrollBar_2, 3, 1, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(StyleWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton_2.setCheckable(True)
        self.pushButton_2.setChecked(True)
        self.pushButton_2.setFlat(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 4, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(StyleWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.pushButton.setCheckable(True)
        self.pushButton.setChecked(True)
        self.pushButton.setFlat(False)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 4, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem1, 5, 0, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 6, 0, 1, 1)
        self.close = QtWidgets.QPushButton(StyleWidget)
        self.close.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.close.setObjectName("close")
        self.gridLayout.addWidget(self.close, 6, 1, 1, 1)

        self.retranslateUi(StyleWidget)
        self.horizontalScrollBar.valueChanged['int'].connect(self.horizontalScrollBar_2.setValue)
        self.horizontalScrollBar_2.valueChanged['int'].connect(self.horizontalScrollBar.setValue)
        self.pushButton.clicked['bool'].connect(self.horizontalScrollBar_2.setEnabled)
        self.pushButton_2.clicked['bool'].connect(self.horizontalScrollBar.setVisible)
        self.spinBox.valueChanged['int'].connect(self.horizontalScrollBar_2.setValue)
        self.horizontalScrollBar_2.valueChanged['int'].connect(self.spinBox.setValue)
        QtCore.QMetaObject.connectSlotsByName(StyleWidget)

    def retranslateUi(self, StyleWidget):
        _translate = QtCore.QCoreApplication.translate
        StyleWidget.setWindowTitle(_translate("StyleWidget", "Form"))
        self.groupBox.setTitle(_translate("StyleWidget", "Styles"))
        self.transparentStyle.setText(_translate("StyleWidget", "Transp."))
        self.blueStyle.setText(_translate("StyleWidget", "Blue"))
        self.khakiStyle.setText(_translate("StyleWidget", "Khaki"))
        self.noStyle.setText(_translate("StyleWidget", "None"))
        self.label.setText(_translate("StyleWidget", "Value:"))
        self.pushButton_2.setText(_translate("StyleWidget", "Show"))
        self.pushButton.setText(_translate("StyleWidget", "Enable"))
        self.close.setText(_translate("StyleWidget", "Close"))


import styleexample_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    StyleWidget = QtWidgets.QWidget()
    ui = Ui_StyleWidget()
    ui.setupUi(StyleWidget)
    StyleWidget.show()
    sys.exit(app.exec_())
