/**
 * @file Builder.h
 *
 * @brief @todo
 */
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


/**
 * @brief Builderは@todoのクラス。
 *
 * @todo
 */
class Builder {
private:
  /**
   * @brief ToolBarActionは@todoの構造体。
   *
   * @todo
   */
  struct ToolBarAction {
    QAction* m_action = nullptr;
    QToolButton* m_button = nullptr;
  };

public:
  /**
   * @brief @todo
   *
   * @todo
   */
  static Builder* getInstance();

  /**
   * @brief @todo
   *
   * @todo \a mainWindow  \a ui
   */
  void build(MainWindow* mainWindow, Ui::MainWindow* ui);

private:
  /**
   * @brief @todo
   *
   * @todo \a mainWindow  \a ui
   */
  void buildGraphicsView(MainWindow* mainWindow, Ui::MainWindow* ui);

  /**
   * @brief @todo
   *
   * @todo \a mainWindow  \a ui
   */
  void buildMenuBar(MainWindow* mainWindow, Ui::MainWindow* ui);

  /**
   * @brief @todo
   *
   * @todo \a mainWindow  \a ui
   */
  void buildToolBar(MainWindow* mainWindow, Ui::MainWindow* ui);

  /**
   * @brief @todo
   *
   * @todo \a mainWindow  \a ui
   */
  void buildWindowTitle(MainWindow* mainWindow, Ui::MainWindow* ui);

  /**
   * @brief @todo
   *
   * @todo \a mainWindow  \a ui
   */
  void buildDockWidget(MainWindow* mainWindow, Ui::MainWindow* ui);

private:
  /// @todo
  QMap<QString, ToolBarAction*> toolBarActions_;

private:
  /**
   * @brief コンストラクタ
   *
   * @todo
   */
  Builder();

  /**
   * @brief デストラクタ
   *
   * @todo
   */
  ~Builder();
};

#endif // BUILDER_H
