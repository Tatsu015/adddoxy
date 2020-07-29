#ifndef BUILDER_H
#define BUILDER_H

#include <QMap>
#include <QString>

class QAction;
class QToolButton;
class MainWindow;

namespace Ui {
class MainWindow;
}

class Builder {
private:
  struct ToolBarAction {
    QAction* m_action = nullptr;
    QToolButton* m_button = nullptr;
  };

public:
  static Builder* getInstance();
  void build(MainWindow* mainWindow, Ui::MainWindow* ui);

private:
  void buildGraphicsView(MainWindow* mainWindow, Ui::MainWindow* ui);
  void buildMenuBar(MainWindow* mainWindow, Ui::MainWindow* ui);
  void buildToolBar(MainWindow* mainWindow, Ui::MainWindow* ui);
  void buildWindowTitle(MainWindow* mainWindow, Ui::MainWindow* ui);
  void buildDockWidget(MainWindow* mainWindow, Ui::MainWindow* ui);

private:
  QMap<QString, ToolBarAction*> toolBarActions_;

private:
  Builder();
  ~Builder();
};

#endif // BUILDER_H
